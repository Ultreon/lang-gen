from __future__ import annotations
from overload import overload


 
import dev.ultreon.libs.functions.v0.supplier.CharSupplier as __CharSupplier
__CharSupplier = __CharSupplier
from pyquantum_helper import override
import java.lang.Character as __Character
__Character = __Character
import java.lang.Character as Character
from abc import abstractmethod, ABC
 
class CharSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.CharSupplier"""
 
    @staticmethod
    def __wrap(java_value: __CharSupplier) -> 'CharSupplier':
        return CharSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSupplier):
        """
        Dynamic initializer for CharSupplier.
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
    def getChar(self, ):
        """public abstract char dev.ultreon.libs.functions.v0.supplier.CharSupplier.getChar()"""
        pass

    @override
    @overload
    def get(self) -> 'Character':
        """public default java.lang.Character dev.ultreon.libs.functions.v0.supplier.CharSupplier.get()"""
        return 'Character'.__wrap(super(CharSupplier, self).get())

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.CharSupplier
import dev.ultreon.libs.functions.v0.supplier.CharSupplier as __CharSupplier
__CharSupplier = __CharSupplier
from pyquantum_helper import override
import java.lang.Character as __Character
__Character = __Character
import java.lang.Character as Character
from abc import abstractmethod, ABC
 
class CharSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.CharSupplier"""
 
    @staticmethod
    def __wrap(java_value: __CharSupplier) -> 'CharSupplier':
        return CharSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __CharSupplier):
        """
        Dynamic initializer for CharSupplier.
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
    def getChar(self, ):
        """public abstract char dev.ultreon.libs.functions.v0.supplier.CharSupplier.getChar()"""
        pass

    @override
    @overload
    def get(self) -> 'Character':
        """public default java.lang.Character dev.ultreon.libs.functions.v0.supplier.CharSupplier.get()"""
        return 'Character'.__wrap(super(CharSupplier, self).get())

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.CharSupplier 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.DoubleSupplier
from pyquantum_helper import transform as __transform
import dev.ultreon.libs.functions.v0.supplier.LongSupplier as __LongSupplier
__LongSupplier = __LongSupplier
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.DoubleSupplier as __DoubleSupplier
__DoubleSupplier = __DoubleSupplier
from abc import abstractmethod, ABC
import java.lang.Double as Double
 
class DoubleSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.DoubleSupplier"""
 
    @staticmethod
    def __wrap(java_value: __DoubleSupplier) -> 'DoubleSupplier':
        return DoubleSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __DoubleSupplier):
        """
        Dynamic initializer for DoubleSupplier.
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
    def acos(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.acos()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).acos())

    @overload
    def atan2(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'.__wrap(super(__DoubleSupplier, self).atan2(arg0))

    @overload
    def add(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.add(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'.__wrap(super(__DoubleSupplier, self).add(arg0))

    @overload
    def pow(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.pow(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'.__wrap(super(__DoubleSupplier, self).pow(arg0))

    @overload
    def sinh(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sinh()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).sinh())

    @overload
    def mod(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.mod(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'.__wrap(super(__DoubleSupplier, self).mod(arg0))

    @overload
    def sqrt(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sqrt()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).sqrt())

    @overload
    def asin(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.asin()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).asin())

    @overload
    def tan(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.tan()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).tan())

    @overload
    def roundDouble(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.roundDouble()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).roundDouble())

    @overload
    def sin(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sin()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).sin())

    @overload
    def mul(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.mul(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'.__wrap(super(__DoubleSupplier, self).mul(arg0))

    @overload
    def cosh(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.cosh()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).cosh())

    @abstractmethod
    def getDouble(self, ):
        """public abstract double dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.getDouble()"""
        pass

    @overload
    def atan(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.atan()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).atan())

    @overload
    def cos(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.cos()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).cos())

    @override
    @overload
    def get(self) -> 'Double':
        """public default java.lang.Double dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.get()"""
        return __transform(super(DoubleSupplier, self).get()).'Double'Value()

    @overload
    def div(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.div(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'.__wrap(super(__DoubleSupplier, self).div(arg0))

    @overload
    def sub(self, arg0: 'DoubleSupplier') -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.sub(dev.ultreon.libs.functions.v0.supplier.DoubleSupplier)"""
        return 'DoubleSupplier'.__wrap(super(__DoubleSupplier, self).sub(arg0))

    @overload
    def round(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.round()"""
        return 'LongSupplier'.__wrap(super(DoubleSupplier, self).round())

    @overload
    def tanh(self) -> 'DoubleSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.DoubleSupplier dev.ultreon.libs.functions.v0.supplier.DoubleSupplier.tanh()"""
        return 'DoubleSupplier'.__wrap(super(DoubleSupplier, self).tanh()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.FloatSupplier
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.IntSupplier as __IntSupplier
__IntSupplier = __IntSupplier
import java.lang.Float as Float
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.supplier.FloatSupplier as __FloatSupplier
__FloatSupplier = __FloatSupplier
 
class FloatSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.FloatSupplier"""
 
    @staticmethod
    def __wrap(java_value: __FloatSupplier) -> 'FloatSupplier':
        return FloatSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FloatSupplier):
        """
        Dynamic initializer for FloatSupplier.
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
    def asin(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.asin()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).asin())

    @overload
    def atan(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.atan()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).atan())

    @overload
    def round(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.round()"""
        return 'IntSupplier'.__wrap(super(FloatSupplier, self).round())

    @overload
    def sinh(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sinh()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).sinh())

    @overload
    def atan2(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'.__wrap(super(__FloatSupplier, self).atan2(arg0))

    @overload
    def add(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.add(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'.__wrap(super(__FloatSupplier, self).add(arg0))

    @overload
    def tanh(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.tanh()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).tanh())

    @overload
    def div(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.div(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'.__wrap(super(__FloatSupplier, self).div(arg0))

    @overload
    def mul(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.mul(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'.__wrap(super(__FloatSupplier, self).mul(arg0))

    @overload
    def cos(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.cos()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).cos())

    @override
    @overload
    def get(self) -> 'Float':
        """public default java.lang.Float dev.ultreon.libs.functions.v0.supplier.FloatSupplier.get()"""
        return __transform(super(FloatSupplier, self).get()).'Float'Value()

    @overload
    def roundFloat(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.roundFloat()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).roundFloat())

    @overload
    def tan(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.tan()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).tan())

    @overload
    def sub(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sub(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'.__wrap(super(__FloatSupplier, self).sub(arg0))

    @overload
    def cosh(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.cosh()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).cosh())

    @overload
    def sqrt(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sqrt()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).sqrt())

    @overload
    def acos(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.acos()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).acos())

    @abstractmethod
    def getFloat(self, ):
        """public abstract float dev.ultreon.libs.functions.v0.supplier.FloatSupplier.getFloat()"""
        pass

    @overload
    def sin(self) -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.sin()"""
        return 'FloatSupplier'.__wrap(super(FloatSupplier, self).sin())

    @overload
    def mod(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.mod(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'.__wrap(super(__FloatSupplier, self).mod(arg0))

    @overload
    def pow(self, arg0: 'FloatSupplier') -> 'FloatSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.FloatSupplier dev.ultreon.libs.functions.v0.supplier.FloatSupplier.pow(dev.ultreon.libs.functions.v0.supplier.FloatSupplier)"""
        return 'FloatSupplier'.__wrap(super(__FloatSupplier, self).pow(arg0)) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.BooleanSupplier
import java.lang.Boolean as Boolean
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.BooleanSupplier as __BooleanSupplier
__BooleanSupplier = __BooleanSupplier
import java.lang.Boolean as __Boolean
__Boolean = __Boolean
from abc import abstractmethod, ABC
 
class BooleanSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.BooleanSupplier"""
 
    @staticmethod
    def __wrap(java_value: __BooleanSupplier) -> 'BooleanSupplier':
        return BooleanSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __BooleanSupplier):
        """
        Dynamic initializer for BooleanSupplier.
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
    def getBoolean(self, ):
        """public abstract boolean dev.ultreon.libs.functions.v0.supplier.BooleanSupplier.getBoolean()"""
        pass

    @override
    @overload
    def get(self) -> 'Boolean':
        """public default java.lang.Boolean dev.ultreon.libs.functions.v0.supplier.BooleanSupplier.get()"""
        return 'Boolean'.__wrap(super(BooleanSupplier, self).get()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.ShortSupplier
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Short as Short
import dev.ultreon.libs.functions.v0.supplier.ShortSupplier as __ShortSupplier
__ShortSupplier = __ShortSupplier
from abc import abstractmethod, ABC
 
class ShortSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.ShortSupplier"""
 
    @staticmethod
    def __wrap(java_value: __ShortSupplier) -> 'ShortSupplier':
        return ShortSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ShortSupplier):
        """
        Dynamic initializer for ShortSupplier.
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
    def cos(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.cos()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).cos())

    @overload
    def round(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.round()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).round())

    @overload
    def atan(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.atan()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).atan())

    @overload
    def atan2(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).atan2(arg0))

    @overload
    def tan(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.tan()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).tan())

    @overload
    def asin(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.asin()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).asin())

    @overload
    def pow(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.pow(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).pow(arg0))

    @overload
    def div(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.div(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).div(arg0))

    @overload
    def tanh(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.tanh()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).tanh())

    @overload
    def sub(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sub(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).sub(arg0))

    @overload
    def cosh(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.cosh()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).cosh())

    @overload
    def add(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.add(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).add(arg0))

    @abstractmethod
    def getShort(self, ):
        """public abstract short dev.ultreon.libs.functions.v0.supplier.ShortSupplier.getShort()"""
        pass

    @override
    @overload
    def get(self) -> 'Short':
        """public default java.lang.Short dev.ultreon.libs.functions.v0.supplier.ShortSupplier.get()"""
        return __transform(super(ShortSupplier, self).get()).'Short'Value()

    @overload
    def sqrt(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sqrt()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).sqrt())

    @overload
    def mul(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.mul(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).mul(arg0))

    @overload
    def mod(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.mod(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).mod(arg0))

    @overload
    def acos(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.acos()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).acos())

    @overload
    def sinh(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sinh()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).sinh())

    @overload
    def sin(self) -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.sin()"""
        return 'ShortSupplier'.__wrap(super(ShortSupplier, self).sin())

    @overload
    def or(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.or(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).or(arg0))

    @overload
    def and(self, arg0: 'ShortSupplier') -> 'ShortSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ShortSupplier dev.ultreon.libs.functions.v0.supplier.ShortSupplier.and(dev.ultreon.libs.functions.v0.supplier.ShortSupplier)"""
        return 'ShortSupplier'.__wrap(super(__ShortSupplier, self).and(arg0)) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.LongSupplier
import dev.ultreon.libs.functions.v0.supplier.LongSupplier as __LongSupplier
__LongSupplier = __LongSupplier
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import java.lang.Long as Long
from abc import abstractmethod, ABC
 
class LongSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.LongSupplier"""
 
    @staticmethod
    def __wrap(java_value: __LongSupplier) -> 'LongSupplier':
        return LongSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __LongSupplier):
        """
        Dynamic initializer for LongSupplier.
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
    def sinh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sinh()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).sinh())

    @overload
    def and(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.and(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).and(arg0))

    @overload
    def atan2(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).atan2(arg0))

    @overload
    def mul(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.mul(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).mul(arg0))

    @overload
    def round(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.round()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).round())

    @overload
    def cos(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.cos()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).cos())

    @overload
    def pow(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.pow(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).pow(arg0))

    @overload
    def cosh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.cosh()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).cosh())

    @overload
    def tanh(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.tanh()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).tanh())

    @abstractmethod
    def getLong(self, ):
        """public abstract long dev.ultreon.libs.functions.v0.supplier.LongSupplier.getLong()"""
        pass

    @overload
    def div(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.div(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).div(arg0))

    @override
    @overload
    def get(self) -> 'Long':
        """public default java.lang.Long dev.ultreon.libs.functions.v0.supplier.LongSupplier.get()"""
        return __transform(super(LongSupplier, self).get()).'Long'Value()

    @overload
    def sin(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sin()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).sin())

    @overload
    def asin(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.asin()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).asin())

    @overload
    def or(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.or(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).or(arg0))

    @overload
    def sub(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sub(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).sub(arg0))

    @overload
    def add(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.add(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).add(arg0))

    @overload
    def acos(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.acos()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).acos())

    @overload
    def mod(self, arg0: 'LongSupplier') -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.mod(dev.ultreon.libs.functions.v0.supplier.LongSupplier)"""
        return 'LongSupplier'.__wrap(super(__LongSupplier, self).mod(arg0))

    @overload
    def sqrt(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.sqrt()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).sqrt())

    @overload
    def tan(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.tan()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).tan())

    @overload
    def atan(self) -> 'LongSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.LongSupplier dev.ultreon.libs.functions.v0.supplier.LongSupplier.atan()"""
        return 'LongSupplier'.__wrap(super(LongSupplier, self).atan()) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.IntSupplier
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.IntSupplier as __IntSupplier
__IntSupplier = __IntSupplier
import java.lang.Integer as Integer
from abc import abstractmethod, ABC
 
class IntSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.IntSupplier"""
 
    @staticmethod
    def __wrap(java_value: __IntSupplier) -> 'IntSupplier':
        return IntSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __IntSupplier):
        """
        Dynamic initializer for IntSupplier.
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
    def sinh(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sinh()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).sinh())

    @overload
    def sin(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sin()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).sin())

    @overload
    def mod(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.mod(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).mod(arg0))

    @overload
    def add(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.add(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).add(arg0))

    @overload
    def acos(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.acos()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).acos())

    @overload
    def cosh(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.cosh()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).cosh())

    @overload
    def mul(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.mul(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).mul(arg0))

    @overload
    def atan(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.atan()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).atan())

    @overload
    def sqrt(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sqrt()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).sqrt())

    @overload
    def pow(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.pow(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).pow(arg0))

    @overload
    def round(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.round()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).round())

    @overload
    def tan(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.tan()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).tan())

    @overload
    def div(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.div(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).div(arg0))

    @overload
    def tanh(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.tanh()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).tanh())

    @override
    @overload
    def get(self) -> 'Integer':
        """public default java.lang.Integer dev.ultreon.libs.functions.v0.supplier.IntSupplier.get()"""
        return __transform(super(IntSupplier, self).get()).'Integer'Value()

    @overload
    def asin(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.asin()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).asin())

    @overload
    def and(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.and(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).and(arg0))

    @overload
    def atan2(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).atan2(arg0))

    @abstractmethod
    def getInt(self, ):
        """public abstract int dev.ultreon.libs.functions.v0.supplier.IntSupplier.getInt()"""
        pass

    @overload
    def cos(self) -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.cos()"""
        return 'IntSupplier'.__wrap(super(IntSupplier, self).cos())

    @overload
    def sub(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.sub(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).sub(arg0))

    @overload
    def or(self, arg0: 'IntSupplier') -> 'IntSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.IntSupplier dev.ultreon.libs.functions.v0.supplier.IntSupplier.or(dev.ultreon.libs.functions.v0.supplier.IntSupplier)"""
        return 'IntSupplier'.__wrap(super(__IntSupplier, self).or(arg0)) 
 
 
# CLASS: dev.ultreon.libs.functions.v0.supplier.ByteSupplier
from pyquantum_helper import transform as __transform
from pyquantum_helper import override
import dev.ultreon.libs.functions.v0.supplier.ByteSupplier as __ByteSupplier
__ByteSupplier = __ByteSupplier
from abc import abstractmethod, ABC
import java.lang.Byte as Byte
 
class ByteSupplier(ABC):
    """dev.ultreon.libs.functions.v0.supplier.ByteSupplier"""
 
    @staticmethod
    def __wrap(java_value: __ByteSupplier) -> 'ByteSupplier':
        return ByteSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ByteSupplier):
        """
        Dynamic initializer for ByteSupplier.
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
    def sin(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sin()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).sin())

    @overload
    def tan(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.tan()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).tan())

    @overload
    def atan(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.atan()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).atan())

    @overload
    def pow(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.pow(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).pow(arg0))

    @overload
    def asin(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.asin()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).asin())

    @overload
    def add(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.add(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).add(arg0))

    @overload
    def and(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.and(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).and(arg0))

    @overload
    def atan2(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.atan2(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).atan2(arg0))

    @overload
    def tanh(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.tanh()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).tanh())

    @overload
    def div(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.div(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).div(arg0))

    @override
    @overload
    def get(self) -> 'Byte':
        """public default java.lang.Byte dev.ultreon.libs.functions.v0.supplier.ByteSupplier.get()"""
        return __transform(super(ByteSupplier, self).get()).'Byte'Value()

    @abstractmethod
    def getByte(self, ):
        """public abstract byte dev.ultreon.libs.functions.v0.supplier.ByteSupplier.getByte()"""
        pass

    @overload
    def sqrt(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sqrt()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).sqrt())

    @overload
    def cos(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.cos()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).cos())

    @overload
    def or(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.or(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).or(arg0))

    @overload
    def cosh(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.cosh()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).cosh())

    @overload
    def round(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.round()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).round())

    @overload
    def mod(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.mod(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).mod(arg0))

    @overload
    def acos(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.acos()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).acos())

    @overload
    def sinh(self) -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sinh()"""
        return 'ByteSupplier'.__wrap(super(ByteSupplier, self).sinh())

    @overload
    def sub(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.sub(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).sub(arg0))

    @overload
    def mul(self, arg0: 'ByteSupplier') -> 'ByteSupplier':
        """public default dev.ultreon.libs.functions.v0.supplier.ByteSupplier dev.ultreon.libs.functions.v0.supplier.ByteSupplier.mul(dev.ultreon.libs.functions.v0.supplier.ByteSupplier)"""
        return 'ByteSupplier'.__wrap(super(__ByteSupplier, self).mul(arg0))