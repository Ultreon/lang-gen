from __future__ import annotations
from overload import overload


 
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Long as Long
import dev.ultreon.libs.functions.v0.supplier.LongSupplier as _LongSupplier
_LongSupplier = _LongSupplier
from abc import abstractmethod, ABC
 
class LongSupplier():
    """dev.ultreon.libs.functions.v0.supplier.LongSupplier"""
 
    @staticmethod
    def _wrap(java_value: _LongSupplier) -> 'LongSupplier':
        return LongSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongSupplier):
        """
        Dynamic initializer for LongSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mod(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.mod(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).mod(arg0))

    @overload
    def round(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.round()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).round())

    @overload
    def asin(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.asin()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).asin())

    @overload
    def and(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.and(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).and(arg0))

    @overload
    def div(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.div(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).div(arg0))

    @overload
    def sqrt(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sqrt()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).sqrt())

    @abstractmethod
    def getLong(self, ):
        """public abstract long dev.ultreon.libs.functions.v0.supplier.LongSupplier.getLong()"""
        pass

    @overload
    def add(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.add(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).add(arg0))

    @overload
    def tanh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.tanh()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).tanh())

    @overload
    def or(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.or(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).or(arg0))

    @overload
    def sinh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sinh()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).sinh())

    @overload
    def mul(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.mul(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).mul(arg0))

    @overload
    def atan(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.atan()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).atan())

    @overload
    def cosh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.cosh()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).cosh())

    @overload
    def tan(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.tan()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).tan())

    @overload
    def pow(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.pow(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).pow(arg0))

    @overload
    def cos(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.cos()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).cos())

    @overload
    def acos(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.acos()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).acos())

    @overload
    def sin(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sin()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).sin())

    @override
    @overload
    def get(self) -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.functions.v0.supplier.LongSupplier.get()"""
        return _transform(super(LongSupplier, self).get()).'Long'Value()

    @overload
    def sub(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sub(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).sub(arg0))

    @overload
    def atan2(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).atan2(arg0))

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.LongSupplier
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Long as Long
import dev.ultreon.libs.functions.v0.supplier.LongSupplier as _LongSupplier
_LongSupplier = _LongSupplier
from abc import abstractmethod, ABC
 
class LongSupplier():
    """dev.ultreon.libs.functions.v0.supplier.LongSupplier"""
 
    @staticmethod
    def _wrap(java_value: _LongSupplier) -> 'LongSupplier':
        return LongSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _LongSupplier):
        """
        Dynamic initializer for LongSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_LongSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_LongSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def mod(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.mod(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).mod(arg0))

    @overload
    def round(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.round()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).round())

    @overload
    def asin(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.asin()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).asin())

    @overload
    def and(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.and(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).and(arg0))

    @overload
    def div(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.div(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).div(arg0))

    @overload
    def sqrt(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sqrt()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).sqrt())

    @abstractmethod
    def getLong(self, ):
        """public abstract long dev.ultreon.libs.functions.v0.supplier.LongSupplier.getLong()"""
        pass

    @overload
    def add(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.add(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).add(arg0))

    @overload
    def tanh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.tanh()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).tanh())

    @overload
    def or(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.or(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).or(arg0))

    @overload
    def sinh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sinh()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).sinh())

    @overload
    def mul(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.mul(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).mul(arg0))

    @overload
    def atan(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.atan()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).atan())

    @overload
    def cosh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.cosh()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).cosh())

    @overload
    def tan(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.tan()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).tan())

    @overload
    def pow(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.pow(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).pow(arg0))

    @overload
    def cos(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.cos()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).cos())

    @overload
    def acos(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.acos()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).acos())

    @overload
    def sin(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sin()"""
        return 'LongSupplier'._wrap(super(LongSupplier, self).sin())

    @override
    @overload
    def get(self) -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.functions.v0.supplier.LongSupplier.get()"""
        return _transform(super(LongSupplier, self).get()).'Long'Value()

    @overload
    def sub(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sub(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).sub(arg0))

    @overload
    def atan2(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'._wrap(super(_LongSupplier, self).atan2(arg0))

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.LongSupplier 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.IntSupplier
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.IntSupplier as _IntSupplier
_IntSupplier = _IntSupplier
import java.lang.Integer as Integer
from abc import abstractmethod, ABC
 
class IntSupplier():
    """dev.ultreon.libs.functions.v0.supplier.IntSupplier"""
 
    @staticmethod
    def _wrap(java_value: _IntSupplier) -> 'IntSupplier':
        return IntSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _IntSupplier):
        """
        Dynamic initializer for IntSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_IntSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_IntSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def tan(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.tan()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).tan())

    @overload
    def asin(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.asin()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).asin())

    @overload
    def tanh(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.tanh()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).tanh())

    @overload
    def and(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.and(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).and(arg0))

    @overload
    def add(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.add(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).add(arg0))

    @overload
    def cosh(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.cosh()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).cosh())

    @overload
    def acos(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.acos()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).acos())

    @overload
    def div(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.div(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).div(arg0))

    @overload
    def mod(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.mod(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).mod(arg0))

    @overload
    def atan(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.atan()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).atan())

    @overload
    def sinh(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sinh()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).sinh())

    @overload
    def pow(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.pow(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).pow(arg0))

    @overload
    def round(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.round()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).round())

    @abstractmethod
    def getInt(self, ):
        """public abstract int dev.ultreon.libs.functions.v0.supplier.IntSupplier.getInt()"""
        pass

    @overload
    def sin(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sin()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).sin())

    @overload
    def or(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.or(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).or(arg0))

    @override
    @overload
    def get(self) -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.functions.v0.supplier.IntSupplier.get()"""
        return _transform(super(IntSupplier, self).get()).'Integer'Value()

    @overload
    def cos(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.cos()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).cos())

    @overload
    def sqrt(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sqrt()"""
        return 'IntSupplier'._wrap(super(IntSupplier, self).sqrt())

    @overload
    def mul(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.mul(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).mul(arg0))

    @overload
    def sub(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sub(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).sub(arg0))

    @overload
    def atan2(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'._wrap(super(_IntSupplier, self).atan2(arg0)) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.ShortSupplier
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Short as Short
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.supplier.ShortSupplier as _ShortSupplier
_ShortSupplier = _ShortSupplier
 
class ShortSupplier():
    """dev.ultreon.libs.functions.v0.supplier.ShortSupplier"""
 
    @staticmethod
    def _wrap(java_value: _ShortSupplier) -> 'ShortSupplier':
        return ShortSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ShortSupplier):
        """
        Dynamic initializer for ShortSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ShortSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ShortSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sinh(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sinh()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).sinh())

    @overload
    def tanh(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.tanh()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).tanh())

    @overload
    def asin(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.asin()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).asin())

    @overload
    def tan(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.tan()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).tan())

    @overload
    def atan(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.atan()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).atan())

    @override
    @overload
    def get(self) -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.functions.v0.supplier.ShortSupplier.get()"""
        return _transform(super(ShortSupplier, self).get()).'Short'Value()

    @overload
    def sin(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sin()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).sin())

    @overload
    def cos(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.cos()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).cos())

    @overload
    def add(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.add(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).add(arg0))

    @overload
    def acos(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.acos()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).acos())

    @overload
    def and(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.and(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).and(arg0))

    @overload
    def round(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.round()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).round())

    @overload
    def cosh(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.cosh()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).cosh())

    @overload
    def mul(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.mul(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).mul(arg0))

    @abstractmethod
    def getShort(self, ):
        """public abstract short dev.ultreon.libs.functions.v0.supplier.ShortSupplier.getShort()"""
        pass

    @overload
    def mod(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.mod(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).mod(arg0))

    @overload
    def div(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.div(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).div(arg0))

    @overload
    def pow(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.pow(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).pow(arg0))

    @overload
    def sub(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sub(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).sub(arg0))

    @overload
    def atan2(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).atan2(arg0))

    @overload
    def or(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.or(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'._wrap(super(_ShortSupplier, self).or(arg0))

    @overload
    def sqrt(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sqrt()"""
        return 'ShortSupplier'._wrap(super(ShortSupplier, self).sqrt()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.BooleanSupplier
import java.lang.Boolean as Boolean
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.BooleanSupplier as _BooleanSupplier
_BooleanSupplier = _BooleanSupplier
from abc import abstractmethod, ABC
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
 
class BooleanSupplier():
    """dev.ultreon.libs.functions.v0.supplier.BooleanSupplier"""
 
    @staticmethod
    def _wrap(java_value: _BooleanSupplier) -> 'BooleanSupplier':
        return BooleanSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _BooleanSupplier):
        """
        Dynamic initializer for BooleanSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_BooleanSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_BooleanSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getBoolean(self, ):
        """public abstract boolean dev.ultreon.libs.functions.v0.supplier.BooleanSupplier.getBoolean()"""
        pass

    @override
    @overload
    def get(self) -> 'Boolean':
        """public default java.lang.Boolean dev.ultreon.libs.functions.v0.supplier.BooleanSupplier.get()"""
        return 'Boolean'._wrap(super(BooleanSupplier, self).get()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.FloatSupplier
import dev.ultreon.libs.functions.v0.supplier.FloatSupplier as _FloatSupplier
_FloatSupplier = _FloatSupplier
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.IntSupplier as _IntSupplier
_IntSupplier = _IntSupplier
import java.lang.Float as Float
from abc import abstractmethod, ABC
 
class FloatSupplier():
    """dev.ultreon.libs.functions.v0.supplier.FloatSupplier"""
 
    @staticmethod
    def _wrap(java_value: _FloatSupplier) -> 'FloatSupplier':
        return FloatSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FloatSupplier):
        """
        Dynamic initializer for FloatSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FloatSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FloatSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def sin(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sin()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).sin())

    @overload
    def round(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.round()"""
        return 'IntSupplier'._wrap(super(FloatSupplier, self).round())

    @overload
    def atan2(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'._wrap(super(_FloatSupplier, self).atan2(arg0))

    @overload
    def asin(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.asin()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).asin())

    @overload
    def cosh(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.cosh()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).cosh())

    @overload
    def tan(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.tan()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).tan())

    @overload
    def tanh(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.tanh()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).tanh())

    @overload
    def add(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.add(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'._wrap(super(_FloatSupplier, self).add(arg0))

    @overload
    def mul(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.mul(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'._wrap(super(_FloatSupplier, self).mul(arg0))

    @overload
    def cos(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.cos()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).cos())

    @overload
    def sqrt(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sqrt()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).sqrt())

    @overload
    def pow(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.pow(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'._wrap(super(_FloatSupplier, self).pow(arg0))

    @overload
    def acos(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.acos()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).acos())

    @overload
    def div(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.div(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'._wrap(super(_FloatSupplier, self).div(arg0))

    @overload
    def roundFloat(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.roundFloat()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).roundFloat())

    @overload
    def mod(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.mod(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'._wrap(super(_FloatSupplier, self).mod(arg0))

    @override
    @overload
    def get(self) -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.functions.v0.supplier.FloatSupplier.get()"""
        return _transform(super(FloatSupplier, self).get()).'Float'Value()

    @abstractmethod
    def getFloat(self, ):
        """public abstract float dev.ultreon.libs.functions.v0.supplier.FloatSupplier.getFloat()"""
        pass

    @overload
    def sub(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sub(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'._wrap(super(_FloatSupplier, self).sub(arg0))

    @overload
    def atan(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.atan()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).atan())

    @overload
    def sinh(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sinh()"""
        return 'FloatSupplier'._wrap(super(FloatSupplier, self).sinh()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.CharSupplier
from pyquantum_helper import override
import java.lang.Character as _Character
_Character = _Character
import dev.ultreon.libs.functions.v0.supplier.CharSupplier as _CharSupplier
_CharSupplier = _CharSupplier
import java.lang.Character as Character
from abc import abstractmethod, ABC
 
class CharSupplier():
    """dev.ultreon.libs.functions.v0.supplier.CharSupplier"""
 
    @staticmethod
    def _wrap(java_value: _CharSupplier) -> 'CharSupplier':
        return CharSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CharSupplier):
        """
        Dynamic initializer for CharSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CharSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CharSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getChar(self, ):
        """public abstract char dev.ultreon.libs.functions.v0.supplier.CharSupplier.getChar()"""
        pass

    @override
    @overload
    def get(self) -> 'Character':
        """public default java.lang.Character dev.ultreon.libs.functions.v0.supplier.CharSupplier.get()"""
        return 'Character'._wrap(super(CharSupplier, self).get()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.ByteSupplier
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.ByteSupplier as _ByteSupplier
_ByteSupplier = _ByteSupplier
from abc import abstractmethod, ABC
import java.lang.Byte as Byte
 
class ByteSupplier():
    """dev.ultreon.libs.functions.v0.supplier.ByteSupplier"""
 
    @staticmethod
    def _wrap(java_value: _ByteSupplier) -> 'ByteSupplier':
        return ByteSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ByteSupplier):
        """
        Dynamic initializer for ByteSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ByteSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ByteSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def tan(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.tan()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).tan())

    @overload
    def sub(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sub(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).sub(arg0))

    @overload
    def and(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.and(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).and(arg0))

    @overload
    def cos(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.cos()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).cos())

    @override
    @overload
    def get(self) -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.functions.v0.supplier.ByteSupplier.get()"""
        return _transform(super(ByteSupplier, self).get()).'Byte'Value()

    @overload
    def atan2(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).atan2(arg0))

    @abstractmethod
    def getByte(self, ):
        """public abstract byte dev.ultreon.libs.functions.v0.supplier.ByteSupplier.getByte()"""
        pass

    @overload
    def or(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.or(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).or(arg0))

    @overload
    def sinh(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sinh()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).sinh())

    @overload
    def sin(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sin()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).sin())

    @overload
    def asin(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.asin()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).asin())

    @overload
    def sqrt(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sqrt()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).sqrt())

    @overload
    def mod(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.mod(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).mod(arg0))

    @overload
    def atan(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.atan()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).atan())

    @overload
    def mul(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.mul(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).mul(arg0))

    @overload
    def cosh(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.cosh()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).cosh())

    @overload
    def add(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.add(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).add(arg0))

    @overload
    def div(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.div(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).div(arg0))

    @overload
    def pow(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.pow(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'._wrap(super(_ByteSupplier, self).pow(arg0))

    @overload
    def tanh(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.tanh()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).tanh())

    @overload
    def acos(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.acos()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).acos())

    @overload
    def round(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.round()"""
        return 'ByteSupplier'._wrap(super(ByteSupplier, self).round()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.DoubleSupplier
import dev.ultreon.libs.functions.v0.supplier.DoubleSupplier as _DoubleSupplier
_DoubleSupplier = _DoubleSupplier
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.LongSupplier as _LongSupplier
_LongSupplier = _LongSupplier
from abc import abstractmethod, ABC
import java.lang.Double as Double
 
class DoubleSupplier():
    """dev.ultreon.libs.functions.v0.supplier.DoubleSupplier"""
 
    @staticmethod
    def _wrap(java_value: _DoubleSupplier) -> 'DoubleSupplier':
        return DoubleSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DoubleSupplier):
        """
        Dynamic initializer for DoubleSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DoubleSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DoubleSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def round(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.round()"""
        return 'LongSupplier'._wrap(super(DoubleSupplier, self).round())

    @overload
    def sinh(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sinh()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).sinh())

    @overload
    def mul(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.mul(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'._wrap(super(_DoubleSupplier, self).mul(arg0))

    @overload
    def roundDouble(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.roundDouble()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).roundDouble())

    @overload
    def tanh(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.tanh()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).tanh())

    @override
    @overload
    def get(self) -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.get()"""
        return _transform(super(DoubleSupplier, self).get()).'Double'Value()

    @overload
    def sin(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sin()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).sin())

    @overload
    def tan(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.tan()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).tan())

    @overload
    def atan2(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'._wrap(super(_DoubleSupplier, self).atan2(arg0))

    @overload
    def asin(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.asin()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).asin())

    @overload
    def sqrt(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sqrt()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).sqrt())

    @overload
    def cos(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.cos()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).cos())

    @overload
    def sub(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sub(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'._wrap(super(_DoubleSupplier, self).sub(arg0))

    @overload
    def div(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.div(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'._wrap(super(_DoubleSupplier, self).div(arg0))

    @abstractmethod
    def getDouble(self, ):
        """public abstract double dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.getDouble()"""
        pass

    @overload
    def mod(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.mod(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'._wrap(super(_DoubleSupplier, self).mod(arg0))

    @overload
    def add(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.add(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'._wrap(super(_DoubleSupplier, self).add(arg0))

    @overload
    def acos(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.acos()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).acos())

    @overload
    def atan(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.atan()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).atan())

    @overload
    def cosh(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.cosh()"""
        return 'DoubleSupplier'._wrap(super(DoubleSupplier, self).cosh())

    @overload
    def pow(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.pow(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'._wrap(super(_DoubleSupplier, self).pow(arg0))