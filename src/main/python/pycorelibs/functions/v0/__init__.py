from __future__ import annotations
from overload import overload


 
import java.lang.Double as _double
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Integer as _int
import dev.ultreon.libs.functions.v0.Double2DoubleFunction as _Double2DoubleFunction
_Double2DoubleFunction = _Double2DoubleFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Double as Double
 
class Double2DoubleFunction():
    """dev.ultreon.libs.functions.v0.Double2DoubleFunction"""
 
    @staticmethod
    def _wrap(java_value: _Double2DoubleFunction) -> 'Double2DoubleFunction':
        return Double2DoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Double2DoubleFunction):
        """
        Dynamic initializer for Double2DoubleFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Double2DoubleFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Double2DoubleFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def acos() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.acos()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.acos())

    @staticmethod
    @overload
    def div(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.div(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.div(_double.valueOf(arg0)))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @staticmethod
    @overload
    def tan() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.tan()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.tan())

    @staticmethod
    @overload
    def atan2(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.atan2(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.atan2(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def tanh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.tanh()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.tanh())

    @staticmethod
    @overload
    def atan() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.atan()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.atan())

    @staticmethod
    @overload
    def log1p() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log1p()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.log1p())

    @staticmethod
    @overload
    def cosh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.cosh()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.cosh())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.scalb(int)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.scalb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sub(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sub(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def sin() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sin()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sin())

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract double dev.ultreon.libs.functions.v0.Double2DoubleFunction.apply(double)"""
        pass

    @staticmethod
    @overload
    def minus() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.minus()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.minus())

    @staticmethod
    @overload
    def pow(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.pow(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.pow(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ceil() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.ceil()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.ceil())

    @staticmethod
    @overload
    def round() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.round()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.round())

    @staticmethod
    @overload
    def sinh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sinh()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sinh())

    @staticmethod
    @overload
    def sqrt() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sqrt()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sqrt())

    @staticmethod
    @overload
    def mul(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.mul(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.mul(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def log10() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log10()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.log10())

    @staticmethod
    @overload
    def asin() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.asin()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.asin())

    @staticmethod
    @overload
    def cos() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.cos()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.cos())

    @staticmethod
    @overload
    def log() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.log())

    @staticmethod
    @overload
    def plus() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.plus()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.plus())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @staticmethod
    @overload
    def signum() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.signum()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.signum())

    @overload
    def apply(self, arg0: 'Double') -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.functions.v0.Double2DoubleFunction.apply(java.lang.Double)"""
        return _transform(super(_Double2DoubleFunction, self).apply(arg0)).'Double'Value()

    @staticmethod
    @overload
    def mod(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.mod(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.mod(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ulp() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.ulp()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.ulp())

    @staticmethod
    @overload
    def add(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.add(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.add(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def floor() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.floor()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.floor())

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Double2DoubleFunction
import java.lang.Double as _double
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Integer as _int
import dev.ultreon.libs.functions.v0.Double2DoubleFunction as _Double2DoubleFunction
_Double2DoubleFunction = _Double2DoubleFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Double as Double
 
class Double2DoubleFunction():
    """dev.ultreon.libs.functions.v0.Double2DoubleFunction"""
 
    @staticmethod
    def _wrap(java_value: _Double2DoubleFunction) -> 'Double2DoubleFunction':
        return Double2DoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Double2DoubleFunction):
        """
        Dynamic initializer for Double2DoubleFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Double2DoubleFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Double2DoubleFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def acos() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.acos()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.acos())

    @staticmethod
    @overload
    def div(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.div(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.div(_double.valueOf(arg0)))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @staticmethod
    @overload
    def tan() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.tan()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.tan())

    @staticmethod
    @overload
    def atan2(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.atan2(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.atan2(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def tanh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.tanh()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.tanh())

    @staticmethod
    @overload
    def atan() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.atan()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.atan())

    @staticmethod
    @overload
    def log1p() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log1p()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.log1p())

    @staticmethod
    @overload
    def cosh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.cosh()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.cosh())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.scalb(int)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.scalb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sub(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sub(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def sin() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sin()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sin())

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract double dev.ultreon.libs.functions.v0.Double2DoubleFunction.apply(double)"""
        pass

    @staticmethod
    @overload
    def minus() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.minus()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.minus())

    @staticmethod
    @overload
    def pow(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.pow(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.pow(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ceil() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.ceil()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.ceil())

    @staticmethod
    @overload
    def round() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.round()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.round())

    @staticmethod
    @overload
    def sinh() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sinh()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sinh())

    @staticmethod
    @overload
    def sqrt() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.sqrt()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.sqrt())

    @staticmethod
    @overload
    def mul(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.mul(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.mul(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def log10() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log10()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.log10())

    @staticmethod
    @overload
    def asin() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.asin()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.asin())

    @staticmethod
    @overload
    def cos() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.cos()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.cos())

    @staticmethod
    @overload
    def log() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.log()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.log())

    @staticmethod
    @overload
    def plus() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.plus()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.plus())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @staticmethod
    @overload
    def signum() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.signum()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.signum())

    @overload
    def apply(self, arg0: 'Double') -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.functions.v0.Double2DoubleFunction.apply(java.lang.Double)"""
        return _transform(super(_Double2DoubleFunction, self).apply(arg0)).'Double'Value()

    @staticmethod
    @overload
    def mod(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.mod(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.mod(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def ulp() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.ulp()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.ulp())

    @staticmethod
    @overload
    def add(arg0: float) -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.add(double)"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.add(_double.valueOf(arg0)))

    @staticmethod
    @overload
    def floor() -> 'Double2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.Double2DoubleFunction dev.ultreon.libs.functions.v0.Double2DoubleFunction.floor()"""
        return Double2DoubleFunction._wrap(_Double2DoubleFunction.floor())

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Double2DoubleFunction 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Float2FloatFunction
from pyquantum_helper import import_once as _import_once
import java.lang.Float as _float
import dev.ultreon.libs.functions.v0.Float2FloatFunction as _Float2FloatFunction
_Float2FloatFunction = _Float2FloatFunction
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Integer as _int
try:
    from pycorelibs.functions.v0 import supplier
except ImportError:
    supplier = _import_once("pycorelibs.functions.v0.supplier")

import java.lang.Float as Float
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class Float2FloatFunction():
    """dev.ultreon.libs.functions.v0.Float2FloatFunction"""
 
    @staticmethod
    def _wrap(java_value: _Float2FloatFunction) -> 'Float2FloatFunction':
        return Float2FloatFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Float2FloatFunction):
        """
        Dynamic initializer for Float2FloatFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Float2FloatFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Float2FloatFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def acos() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.acos()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.acos())

    @staticmethod
    @overload
    def sqrt() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sqrt()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.sqrt())

    @staticmethod
    @overload
    def round() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.round()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.round())

    @staticmethod
    @overload
    def mod(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mod(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.mod(arg0))

    @staticmethod
    @overload
    def minus() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.minus()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.minus())

    @staticmethod
    @overload
    def add(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.add(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.add(arg0))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @staticmethod
    @overload
    def mul(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mul(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.mul(arg0))

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.scalb(int)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.scalb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def tan() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.tan()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.tan())

    @staticmethod
    @overload
    def sub(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sub(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.sub(arg0))

    @staticmethod
    @overload
    def mul(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mul(float)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.mul(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def sin() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sin()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.sin())

    @staticmethod
    @overload
    def pow(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.pow(float)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.pow(_float.valueOf(arg0)))

    @abstractmethod
    def apply(self, arg0: float):
        """public abstract float dev.ultreon.libs.functions.v0.Float2FloatFunction.apply(float)"""
        pass

    @staticmethod
    @overload
    def asin() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.asin()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.asin())

    @staticmethod
    @overload
    def cosh() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.cosh()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.cosh())

    @staticmethod
    @overload
    def pow(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.pow(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.pow(arg0))

    @staticmethod
    @overload
    def ulp() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.ulp()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.ulp())

    @staticmethod
    @overload
    def plus() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.plus()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.plus())

    @staticmethod
    @overload
    def add(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.add(float)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.add(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sub(float)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.sub(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.div(float)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.div(_float.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Float') -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.functions.v0.Float2FloatFunction.apply(java.lang.Float)"""
        return _transform(super(_Float2FloatFunction, self).apply(arg0)).'Float'Value()

    @staticmethod
    @overload
    def cos() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.cos()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.cos())

    @staticmethod
    @overload
    def floor() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.floor()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.floor())

    @staticmethod
    @overload
    def signum() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.signum()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.signum())

    @staticmethod
    @overload
    def tanh() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.tanh()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.tanh())

    @staticmethod
    @overload
    def log1p() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.log1p()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.log1p())

    @staticmethod
    @overload
    def atan2(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.atan2(float)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.atan2(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def log10() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.log10()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.log10())

    @staticmethod
    @overload
    def atan() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.atan()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.atan())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @staticmethod
    @overload
    def sinh() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.sinh()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.sinh())

    @staticmethod
    @overload
    def log() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.log()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.log())

    @staticmethod
    @overload
    def mod(arg0: float) -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.mod(float)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.mod(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: 'FloatSupplier') -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.div(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.div(arg0))

    @staticmethod
    @overload
    def ceil() -> 'Float2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.Float2FloatFunction dev.ultreon.libs.functions.v0.Float2FloatFunction.ceil()"""
        return Float2FloatFunction._wrap(_Float2FloatFunction.ceil()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Short2ShortFunction
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Short as Short
import java.lang.Integer as _int
import dev.ultreon.libs.functions.v0.Short2ShortFunction as _Short2ShortFunction
_Short2ShortFunction = _Short2ShortFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Short as _short
 
class Short2ShortFunction():
    """dev.ultreon.libs.functions.v0.Short2ShortFunction"""
 
    @staticmethod
    def _wrap(java_value: _Short2ShortFunction) -> 'Short2ShortFunction':
        return Short2ShortFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Short2ShortFunction):
        """
        Dynamic initializer for Short2ShortFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Short2ShortFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Short2ShortFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ceil() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.ceil()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.ceil())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract short dev.ultreon.libs.functions.v0.Short2ShortFunction.apply(short)"""
        pass

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.scalb(int)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.scalb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def or(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.or(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.or(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def and(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.and(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.and(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def div(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.div(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.div(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def asin() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.asin()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.asin())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @staticmethod
    @overload
    def acos() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.acos()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.acos())

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.mul(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.mul(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def log10() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.log10()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.log10())

    @staticmethod
    @overload
    def sin() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sin()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.sin())

    @staticmethod
    @overload
    def sqrt() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sqrt()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.sqrt())

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sub(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.sub(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def mod(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.mod(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.mod(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def cosh() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.cosh()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.cosh())

    @staticmethod
    @overload
    def floor() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.floor()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.floor())

    @staticmethod
    @overload
    def log() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.log()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.log())

    @overload
    def apply(self, arg0: 'Short') -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.functions.v0.Short2ShortFunction.apply(java.lang.Short)"""
        return _transform(super(_Short2ShortFunction, self).apply(arg0)).'Short'Value()

    @staticmethod
    @overload
    def signum() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.signum()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.signum())

    @staticmethod
    @overload
    def plus() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.plus()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.plus())

    @staticmethod
    @overload
    def tan() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.tan()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.tan())

    @staticmethod
    @overload
    def atan2(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.atan2(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.atan2(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def tanh() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.tanh()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.tanh())

    @staticmethod
    @overload
    def minus() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.minus()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.minus())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.pow(short)"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.pow(_short.valueOf(arg0)))

    @staticmethod
    @overload
    def atan() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.atan()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.atan())

    @staticmethod
    @overload
    def log1p() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.log1p()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.log1p())

    @staticmethod
    @overload
    def cos() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.cos()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.cos())

    @staticmethod
    @overload
    def ulp() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.ulp()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.ulp())

    @staticmethod
    @overload
    def round() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.round()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.round())

    @staticmethod
    @overload
    def sinh() -> 'Short2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.Short2ShortFunction dev.ultreon.libs.functions.v0.Short2ShortFunction.sinh()"""
        return Short2ShortFunction._wrap(_Short2ShortFunction.sinh()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiByte2ByteFunction
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.BiByte2ByteFunction as _BiByte2ByteFunction
_BiByte2ByteFunction = _BiByte2ByteFunction
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Byte as Byte
import java.util.function.BiFunction as BiFunction
 
class BiByte2ByteFunction():
    """dev.ultreon.libs.functions.v0.BiByte2ByteFunction"""
 
    @staticmethod
    def _wrap(java_value: _BiByte2ByteFunction) -> 'BiByte2ByteFunction':
        return BiByte2ByteFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiByte2ByteFunction):
        """
        Dynamic initializer for BiByte2ByteFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiByte2ByteFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiByte2ByteFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def add() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.add()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.add())

    @staticmethod
    @overload
    def and() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.and()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.and())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'._wrap(super(_BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def pow() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.pow()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.pow())

    @staticmethod
    @overload
    def atan2() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.atan2()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.atan2())

    @staticmethod
    @overload
    def div() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.div()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.div())

    @staticmethod
    @overload
    def or() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.or()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.or())

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract byte dev.ultreon.libs.functions.v0.BiByte2ByteFunction.apply(byte,byte)"""
        pass

    @staticmethod
    @overload
    def sub() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.sub()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.sub())

    @staticmethod
    @overload
    def mul() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.mul()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.mul())

    @staticmethod
    @overload
    def scalb() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.scalb()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.scalb())

    @overload
    def apply(self, arg0: 'Byte', arg1: 'Byte') -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.functions.v0.BiByte2ByteFunction.apply(java.lang.Byte,java.lang.Byte)"""
        return _transform(super(_BiByte2ByteFunction, self).apply(arg0, arg1)).'Byte'Value()

    @staticmethod
    @overload
    def mod() -> 'BiByte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.BiByte2ByteFunction dev.ultreon.libs.functions.v0.BiByte2ByteFunction.mod()"""
        return BiByte2ByteFunction._wrap(_BiByte2ByteFunction.mod()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Int2IntFunction
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import dev.ultreon.libs.functions.v0.Int2IntFunction as _Int2IntFunction
_Int2IntFunction = _Int2IntFunction
import java.lang.Integer as _int
import java.lang.Integer as Integer
from abc import abstractmethod, ABC
import java.util.function.Function as Function
 
class Int2IntFunction():
    """dev.ultreon.libs.functions.v0.Int2IntFunction"""
 
    @staticmethod
    def _wrap(java_value: _Int2IntFunction) -> 'Int2IntFunction':
        return Int2IntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Int2IntFunction):
        """
        Dynamic initializer for Int2IntFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Int2IntFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Int2IntFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def minus() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.minus()"""
        return Int2IntFunction._wrap(_Int2IntFunction.minus())

    @staticmethod
    @overload
    def ulp() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.ulp()"""
        return Int2IntFunction._wrap(_Int2IntFunction.ulp())

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sub(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.sub(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def atan2(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.atan2(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.atan2(_int.valueOf(arg0)))

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @staticmethod
    @overload
    def ceil() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.ceil()"""
        return Int2IntFunction._wrap(_Int2IntFunction.ceil())

    @staticmethod
    @overload
    def log1p() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.log1p()"""
        return Int2IntFunction._wrap(_Int2IntFunction.log1p())

    @staticmethod
    @overload
    def tan() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.tan()"""
        return Int2IntFunction._wrap(_Int2IntFunction.tan())

    @staticmethod
    @overload
    def tanh() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.tanh()"""
        return Int2IntFunction._wrap(_Int2IntFunction.tanh())

    @staticmethod
    @overload
    def plus() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.plus()"""
        return Int2IntFunction._wrap(_Int2IntFunction.plus())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.scalb(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.scalb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def mod(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.mod(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.mod(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def cosh() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.cosh()"""
        return Int2IntFunction._wrap(_Int2IntFunction.cosh())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract int dev.ultreon.libs.functions.v0.Int2IntFunction.apply(int)"""
        pass

    @staticmethod
    @overload
    def div(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.div(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.div(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def or(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.or(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.or(_int.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Integer') -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.functions.v0.Int2IntFunction.apply(java.lang.Integer)"""
        return _transform(super(_Int2IntFunction, self).apply(arg0)).'Integer'Value()

    @staticmethod
    @overload
    def asin() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.asin()"""
        return Int2IntFunction._wrap(_Int2IntFunction.asin())

    @staticmethod
    @overload
    def sqrt() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sqrt()"""
        return Int2IntFunction._wrap(_Int2IntFunction.sqrt())

    @staticmethod
    @overload
    def sin() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sin()"""
        return Int2IntFunction._wrap(_Int2IntFunction.sin())

    @staticmethod
    @overload
    def log() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.log()"""
        return Int2IntFunction._wrap(_Int2IntFunction.log())

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.mul(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.mul(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def round() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.round()"""
        return Int2IntFunction._wrap(_Int2IntFunction.round())

    @staticmethod
    @overload
    def sinh() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.sinh()"""
        return Int2IntFunction._wrap(_Int2IntFunction.sinh())

    @staticmethod
    @overload
    def atan() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.atan()"""
        return Int2IntFunction._wrap(_Int2IntFunction.atan())

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.pow(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.pow(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def acos() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.acos()"""
        return Int2IntFunction._wrap(_Int2IntFunction.acos())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @staticmethod
    @overload
    def log10() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.log10()"""
        return Int2IntFunction._wrap(_Int2IntFunction.log10())

    @staticmethod
    @overload
    def floor() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.floor()"""
        return Int2IntFunction._wrap(_Int2IntFunction.floor())

    @staticmethod
    @overload
    def and(arg0: int) -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.and(int)"""
        return Int2IntFunction._wrap(_Int2IntFunction.and(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def signum() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.signum()"""
        return Int2IntFunction._wrap(_Int2IntFunction.signum())

    @staticmethod
    @overload
    def cos() -> 'Int2IntFunction':
        """public static dev.ultreon.libs.functions.v0.Int2IntFunction dev.ultreon.libs.functions.v0.Int2IntFunction.cos()"""
        return Int2IntFunction._wrap(_Int2IntFunction.cos()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiInt2IntFunction
from pyquantum_helper import transform as _transform
import dev.ultreon.libs.functions.v0.BiInt2IntFunction as _BiInt2IntFunction
_BiInt2IntFunction = _BiInt2IntFunction
from pyquantum_helper import override
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
import java.lang.Integer as Integer
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.function.BiFunction as BiFunction
 
class BiInt2IntFunction():
    """dev.ultreon.libs.functions.v0.BiInt2IntFunction"""
 
    @staticmethod
    def _wrap(java_value: _BiInt2IntFunction) -> 'BiInt2IntFunction':
        return BiInt2IntFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiInt2IntFunction):
        """
        Dynamic initializer for BiInt2IntFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiInt2IntFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiInt2IntFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def mul() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.mul()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.mul())

    @staticmethod
    @overload
    def div() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.div()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.div())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'._wrap(super(_BiFunction, self).andThen(arg0))

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract int dev.ultreon.libs.functions.v0.BiInt2IntFunction.apply(int,int)"""
        pass

    @overload
    def apply(self, arg0: 'Integer', arg1: 'Integer') -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.functions.v0.BiInt2IntFunction.apply(java.lang.Integer,java.lang.Integer)"""
        return _transform(super(_BiInt2IntFunction, self).apply(arg0, arg1)).'Integer'Value()

    @staticmethod
    @overload
    def sub() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.sub()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.sub())

    @staticmethod
    @overload
    def or() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.or()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.or())

    @staticmethod
    @overload
    def and() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.and()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.and())

    @staticmethod
    @overload
    def atan2() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.atan2()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.atan2())

    @staticmethod
    @overload
    def mod() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.mod()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.mod())

    @staticmethod
    @overload
    def scalb() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.scalb()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.scalb())

    @staticmethod
    @overload
    def pow() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.pow()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.pow())

    @staticmethod
    @overload
    def add() -> 'BiInt2IntFunction':
        """public static dev.ultreon.libs.functions.v0.BiInt2IntFunction dev.ultreon.libs.functions.v0.BiInt2IntFunction.add()"""
        return BiInt2IntFunction._wrap(_BiInt2IntFunction.add()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Byte2ByteFunction
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Integer as _int
import java.lang.Byte as _byte
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Byte as Byte
import dev.ultreon.libs.functions.v0.Byte2ByteFunction as _Byte2ByteFunction
_Byte2ByteFunction = _Byte2ByteFunction
 
class Byte2ByteFunction():
    """dev.ultreon.libs.functions.v0.Byte2ByteFunction"""
 
    @staticmethod
    def _wrap(java_value: _Byte2ByteFunction) -> 'Byte2ByteFunction':
        return Byte2ByteFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Byte2ByteFunction):
        """
        Dynamic initializer for Byte2ByteFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Byte2ByteFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Byte2ByteFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def tanh() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.tanh()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.tanh())

    @staticmethod
    @overload
    def log1p() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.log1p()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.log1p())

    @staticmethod
    @overload
    def log10() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.log10()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.log10())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.pow(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.pow(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def ulp() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.ulp()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.ulp())

    @staticmethod
    @overload
    def floor() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.floor()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.floor())

    @staticmethod
    @overload
    def cos() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.cos()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.cos())

    @staticmethod
    @overload
    def cosh() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.cosh()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.cosh())

    @staticmethod
    @overload
    def sinh() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sinh()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.sinh())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract byte dev.ultreon.libs.functions.v0.Byte2ByteFunction.apply(byte)"""
        pass

    @staticmethod
    @overload
    def mod(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.mod(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.mod(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def atan2(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.atan2(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.atan2(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def and(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.and(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.and(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def round() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.round()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.round())

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.scalb(int)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.scalb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sub(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.sub(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def atan() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.atan()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.atan())

    @staticmethod
    @overload
    def ceil() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.ceil()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.ceil())

    @staticmethod
    @overload
    def tan() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.tan()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.tan())

    @staticmethod
    @overload
    def log() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.log()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.log())

    @staticmethod
    @overload
    def acos() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.acos()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.acos())

    @staticmethod
    @overload
    def plus() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.plus()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.plus())

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.mul(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.mul(_byte.valueOf(arg0)))

    @overload
    def apply(self, arg0: 'Byte') -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.functions.v0.Byte2ByteFunction.apply(java.lang.Byte)"""
        return _transform(super(_Byte2ByteFunction, self).apply(arg0)).'Byte'Value()

    @staticmethod
    @overload
    def sqrt() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sqrt()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.sqrt())

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @staticmethod
    @overload
    def sin() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.sin()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.sin())

    @staticmethod
    @overload
    def asin() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.asin()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.asin())

    @staticmethod
    @overload
    def signum() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.signum()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.signum())

    @staticmethod
    @overload
    def or(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.or(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.or(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def minus() -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.minus()"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.minus())

    @staticmethod
    @overload
    def div(arg0: int) -> 'Byte2ByteFunction':
        """public static dev.ultreon.libs.functions.v0.Byte2ByteFunction dev.ultreon.libs.functions.v0.Byte2ByteFunction.div(byte)"""
        return Byte2ByteFunction._wrap(_Byte2ByteFunction.div(_byte.valueOf(arg0))) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiFloat2FloatFunction
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
import dev.ultreon.libs.functions.v0.BiFloat2FloatFunction as _BiFloat2FloatFunction
_BiFloat2FloatFunction = _BiFloat2FloatFunction
import java.lang.Float as Float
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.function.BiFunction as BiFunction
 
class BiFloat2FloatFunction():
    """dev.ultreon.libs.functions.v0.BiFloat2FloatFunction"""
 
    @staticmethod
    def _wrap(java_value: _BiFloat2FloatFunction) -> 'BiFloat2FloatFunction':
        return BiFloat2FloatFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiFloat2FloatFunction):
        """
        Dynamic initializer for BiFloat2FloatFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiFloat2FloatFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiFloat2FloatFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def div() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.div()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.div())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'._wrap(super(_BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def atan2() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.atan2()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.atan2())

    @staticmethod
    @overload
    def mod() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.mod()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.mod())

    @staticmethod
    @overload
    def pow() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.pow()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.pow())

    @abstractmethod
    def apply(self, arg0: float, arg1: float):
        """public abstract float dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.apply(float,float)"""
        pass

    @staticmethod
    @overload
    def scalb() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.scalb()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.scalb())

    @staticmethod
    @overload
    def add() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.add()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.add())

    @overload
    def apply(self, arg0: 'Float', arg1: 'Float') -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.apply(java.lang.Float,java.lang.Float)"""
        return _transform(super(_BiFloat2FloatFunction, self).apply(arg0, arg1)).'Float'Value()

    @staticmethod
    @overload
    def mul() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.mul()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.mul())

    @staticmethod
    @overload
    def sub() -> 'BiFloat2FloatFunction':
        """public static dev.ultreon.libs.functions.v0.BiFloat2FloatFunction dev.ultreon.libs.functions.v0.BiFloat2FloatFunction.sub()"""
        return BiFloat2FloatFunction._wrap(_BiFloat2FloatFunction.sub()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiShort2ShortFunction
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Short as Short
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
import dev.ultreon.libs.functions.v0.BiShort2ShortFunction as _BiShort2ShortFunction
_BiShort2ShortFunction = _BiShort2ShortFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.function.BiFunction as BiFunction
 
class BiShort2ShortFunction():
    """dev.ultreon.libs.functions.v0.BiShort2ShortFunction"""
 
    @staticmethod
    def _wrap(java_value: _BiShort2ShortFunction) -> 'BiShort2ShortFunction':
        return BiShort2ShortFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiShort2ShortFunction):
        """
        Dynamic initializer for BiShort2ShortFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiShort2ShortFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiShort2ShortFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def pow() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.pow()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.pow())

    @staticmethod
    @overload
    def div() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.div()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.div())

    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'._wrap(super(_BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def mod() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.mod()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.mod())

    @staticmethod
    @overload
    def and() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.and()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.and())

    @staticmethod
    @overload
    def mul() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.mul()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.mul())

    @staticmethod
    @overload
    def atan2() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.atan2()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.atan2())

    @staticmethod
    @overload
    def add() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.add()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.add())

    @staticmethod
    @overload
    def or() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.or()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.or())

    @staticmethod
    @overload
    def sub() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.sub()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.sub())

    @staticmethod
    @overload
    def scalb() -> 'BiShort2ShortFunction':
        """public static dev.ultreon.libs.functions.v0.BiShort2ShortFunction dev.ultreon.libs.functions.v0.BiShort2ShortFunction.scalb()"""
        return BiShort2ShortFunction._wrap(_BiShort2ShortFunction.scalb())

    @overload
    def apply(self, arg0: 'Short', arg1: 'Short') -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.functions.v0.BiShort2ShortFunction.apply(java.lang.Short,java.lang.Short)"""
        return _transform(super(_BiShort2ShortFunction, self).apply(arg0, arg1)).'Short'Value()

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract short dev.ultreon.libs.functions.v0.BiShort2ShortFunction.apply(short,short)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.TriFunction
import dev.ultreon.libs.functions.v0.TriFunction as _TriFunction
_TriFunction = _TriFunction
from abc import abstractmethod, ABC
 
class TriFunction():
    """dev.ultreon.libs.functions.v0.TriFunction"""
 
    @staticmethod
    def _wrap(java_value: _TriFunction) -> 'TriFunction':
        return TriFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TriFunction):
        """
        Dynamic initializer for TriFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TriFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TriFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, arg0: object, arg1: object, arg2: object):
        """public abstract R dev.ultreon.libs.functions.v0.TriFunction.apply(A,B,C)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiLong2LongFunction
from pyquantum_helper import transform as _transform
import java.lang.Long as Long
from pyquantum_helper import override
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
import dev.ultreon.libs.functions.v0.BiLong2LongFunction as _BiLong2LongFunction
_BiLong2LongFunction = _BiLong2LongFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.function.BiFunction as BiFunction
 
class BiLong2LongFunction():
    """dev.ultreon.libs.functions.v0.BiLong2LongFunction"""
 
    @staticmethod
    def _wrap(java_value: _BiLong2LongFunction) -> 'BiLong2LongFunction':
        return BiLong2LongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiLong2LongFunction):
        """
        Dynamic initializer for BiLong2LongFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiLong2LongFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiLong2LongFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'._wrap(super(_BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def mul() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.mul()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.mul())

    @staticmethod
    @overload
    def scalb() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.scalb()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.scalb())

    @overload
    def apply(self, arg0: 'Long', arg1: 'Long') -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.functions.v0.BiLong2LongFunction.apply(java.lang.Long,java.lang.Long)"""
        return _transform(super(_BiLong2LongFunction, self).apply(arg0, arg1)).'Long'Value()

    @staticmethod
    @overload
    def mod() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.mod()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.mod())

    @staticmethod
    @overload
    def pow() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.pow()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.pow())

    @staticmethod
    @overload
    def add() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.add()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.add())

    @staticmethod
    @overload
    def atan2() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.atan2()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.atan2())

    @abstractmethod
    def apply(self, arg0: int, arg1: int):
        """public abstract long dev.ultreon.libs.functions.v0.BiLong2LongFunction.apply(long,long)"""
        pass

    @staticmethod
    @overload
    def or() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.or()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.or())

    @staticmethod
    @overload
    def div() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.div()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.div())

    @staticmethod
    @overload
    def sub() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.sub()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.sub())

    @staticmethod
    @overload
    def and() -> 'BiLong2LongFunction':
        """public static dev.ultreon.libs.functions.v0.BiLong2LongFunction dev.ultreon.libs.functions.v0.BiLong2LongFunction.and()"""
        return BiLong2LongFunction._wrap(_BiLong2LongFunction.and()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction
from pyquantum_helper import transform as _transform
import dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction as _BiDouble2DoubleFunction
_BiDouble2DoubleFunction = _BiDouble2DoubleFunction
from pyquantum_helper import override
import java.util.function.BiFunction as _BiFunction
_BiFunction = _BiFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.util.function.BiFunction as BiFunction
import java.lang.Double as Double
 
class BiDouble2DoubleFunction():
    """dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction"""
 
    @staticmethod
    def _wrap(java_value: _BiDouble2DoubleFunction) -> 'BiDouble2DoubleFunction':
        return BiDouble2DoubleFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BiDouble2DoubleFunction):
        """
        Dynamic initializer for BiDouble2DoubleFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BiDouble2DoubleFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BiDouble2DoubleFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def andThen(self, arg0: 'Function') -> 'BiFunction':
        """public default <V> java.util.function.BiFunction<T, U, V> java.util.function.BiFunction.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'BiFunction'._wrap(super(_BiFunction, self).andThen(arg0))

    @staticmethod
    @overload
    def add() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.add()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.add())

    @staticmethod
    @overload
    def atan2() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.atan2()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.atan2())

    @staticmethod
    @overload
    def pow() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.pow()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.pow())

    @staticmethod
    @overload
    def scalb() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.scalb()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.scalb())

    @staticmethod
    @overload
    def sub() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.sub()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.sub())

    @overload
    def apply(self, arg0: 'Double', arg1: 'Double') -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.apply(java.lang.Double,java.lang.Double)"""
        return _transform(super(_BiDouble2DoubleFunction, self).apply(arg0, arg1)).'Double'Value()

    @abstractmethod
    def apply(self, arg0: float, arg1: float):
        """public abstract double dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.apply(double,double)"""
        pass

    @staticmethod
    @overload
    def div() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.div()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.div())

    @staticmethod
    @overload
    def mod() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.mod()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.mod())

    @staticmethod
    @overload
    def mul() -> 'BiDouble2DoubleFunction':
        """public static dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction dev.ultreon.libs.functions.v0.BiDouble2DoubleFunction.mul()"""
        return BiDouble2DoubleFunction._wrap(_BiDouble2DoubleFunction.mul()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.Long2LongFunction
from pyquantum_helper import transform as _transform
import java.lang.Long as Long
from pyquantum_helper import override
import java.util.function.Function as _Function
_Function = _Function
import java.lang.Integer as _int
import dev.ultreon.libs.functions.v0.Long2LongFunction as _Long2LongFunction
_Long2LongFunction = _Long2LongFunction
from abc import abstractmethod, ABC
import java.util.function.Function as Function
import java.lang.Long as _long
 
class Long2LongFunction():
    """dev.ultreon.libs.functions.v0.Long2LongFunction"""
 
    @staticmethod
    def _wrap(java_value: _Long2LongFunction) -> 'Long2LongFunction':
        return Long2LongFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Long2LongFunction):
        """
        Dynamic initializer for Long2LongFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Long2LongFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Long2LongFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def ceil() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.ceil()"""
        return Long2LongFunction._wrap(_Long2LongFunction.ceil())

    @staticmethod
    @overload
    def atan() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.atan()"""
        return Long2LongFunction._wrap(_Long2LongFunction.atan())

    @overload
    def andThen(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<T, V> java.util.function.Function.andThen(java.util.function.Function<? super R, ? extends V>)"""
        return 'Function'._wrap(super(_Function, self).andThen(arg0))

    @staticmethod
    @overload
    def sin() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sin()"""
        return Long2LongFunction._wrap(_Long2LongFunction.sin())

    @staticmethod
    @overload
    def mul(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.mul(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.mul(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def tan() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.tan()"""
        return Long2LongFunction._wrap(_Long2LongFunction.tan())

    @staticmethod
    @overload
    def and(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.and(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.and(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def acos() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.acos()"""
        return Long2LongFunction._wrap(_Long2LongFunction.acos())

    @staticmethod
    @overload
    def plus() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.plus()"""
        return Long2LongFunction._wrap(_Long2LongFunction.plus())

    @staticmethod
    @overload
    def signum() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.signum()"""
        return Long2LongFunction._wrap(_Long2LongFunction.signum())

    @overload
    def apply(self, arg0: 'Long') -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.functions.v0.Long2LongFunction.apply(java.lang.Long)"""
        return _transform(super(_Long2LongFunction, self).apply(arg0)).'Long'Value()

    @staticmethod
    @overload
    def atan2(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.atan2(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.atan2(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def sqrt() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sqrt()"""
        return Long2LongFunction._wrap(_Long2LongFunction.sqrt())

    @staticmethod
    @overload
    def pow(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.pow(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.pow(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def scalb(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.scalb(int)"""
        return Long2LongFunction._wrap(_Long2LongFunction.scalb(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def asin() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.asin()"""
        return Long2LongFunction._wrap(_Long2LongFunction.asin())

    @staticmethod
    @overload
    def cos() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.cos()"""
        return Long2LongFunction._wrap(_Long2LongFunction.cos())

    @staticmethod
    @overload
    def log1p() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.log1p()"""
        return Long2LongFunction._wrap(_Long2LongFunction.log1p())

    @staticmethod
    @overload
    def ulp() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.ulp()"""
        return Long2LongFunction._wrap(_Long2LongFunction.ulp())

    @staticmethod
    @overload
    def round() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.round()"""
        return Long2LongFunction._wrap(_Long2LongFunction.round())

    @staticmethod
    @overload
    def log10() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.log10()"""
        return Long2LongFunction._wrap(_Long2LongFunction.log10())

    @staticmethod
    @overload
    def cosh() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.cosh()"""
        return Long2LongFunction._wrap(_Long2LongFunction.cosh())

    @staticmethod
    @overload
    def div(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.div(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.div(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def tanh() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.tanh()"""
        return Long2LongFunction._wrap(_Long2LongFunction.tanh())

    @staticmethod
    @overload
    def mod(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.mod(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.mod(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def sinh() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sinh()"""
        return Long2LongFunction._wrap(_Long2LongFunction.sinh())

    @staticmethod
    @overload
    def floor() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.floor()"""
        return Long2LongFunction._wrap(_Long2LongFunction.floor())

    @staticmethod
    @overload
    def sub(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.sub(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.sub(_long.valueOf(arg0)))

    @overload
    def compose(self, arg0: 'Function') -> 'Function':
        """public default <V> java.util.function.Function<V, R> java.util.function.Function.compose(java.util.function.Function<? super V, ? extends T>)"""
        return 'Function'._wrap(super(_Function, self).compose(arg0))

    @staticmethod
    @overload
    def minus() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.minus()"""
        return Long2LongFunction._wrap(_Long2LongFunction.minus())

    @staticmethod
    @overload
    def or(arg0: int) -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.or(long)"""
        return Long2LongFunction._wrap(_Long2LongFunction.or(_long.valueOf(arg0)))

    @staticmethod
    @overload
    def log() -> 'Long2LongFunction':
        """public static dev.ultreon.libs.functions.v0.Long2LongFunction dev.ultreon.libs.functions.v0.Long2LongFunction.log()"""
        return Long2LongFunction._wrap(_Long2LongFunction.log())

    @abstractmethod
    def apply(self, arg0: int):
        """public abstract long dev.ultreon.libs.functions.v0.Long2LongFunction.apply(long)"""
        pass