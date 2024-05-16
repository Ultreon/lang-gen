from __future__ import annotations
from overload import overload


 
import dev.ultreon.libs.functions.v0.misc.ThrowingFunction as __ThrowingFunction
__ThrowingFunction = __ThrowingFunction
from abc import abstractmethod, ABC
 
class ThrowingFunction(ABC):
    """dev.ultreon.libs.functions.v0.misc.ThrowingFunction"""
 
    @staticmethod
    def __wrap(java_value: __ThrowingFunction) -> 'ThrowingFunction':
        return ThrowingFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThrowingFunction):
        """
        Dynamic initializer for ThrowingFunction.
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
    def apply(self, arg0: object):
        """public abstract R dev.ultreon.libs.functions.v0.misc.ThrowingFunction.apply(T) throws E"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ThrowingFunction
import dev.ultreon.libs.functions.v0.misc.ThrowingFunction as __ThrowingFunction
__ThrowingFunction = __ThrowingFunction
from abc import abstractmethod, ABC
 
class ThrowingFunction(ABC):
    """dev.ultreon.libs.functions.v0.misc.ThrowingFunction"""
 
    @staticmethod
    def __wrap(java_value: __ThrowingFunction) -> 'ThrowingFunction':
        return ThrowingFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThrowingFunction):
        """
        Dynamic initializer for ThrowingFunction.
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
    def apply(self, arg0: object):
        """public abstract R dev.ultreon.libs.functions.v0.misc.ThrowingFunction.apply(T) throws E"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ThrowingFunction 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.Method
import dev.ultreon.libs.functions.v0.misc.Method as __Method
__Method = __Method
from builtins import object
from abc import abstractmethod, ABC
 
class Method(ABC):
    """dev.ultreon.libs.functions.v0.misc.Method"""
 
    @staticmethod
    def __wrap(java_value: __Method) -> 'Method':
        return Method(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Method):
        """
        Dynamic initializer for Method.
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
    def call(self, arg0: object, *arg1: object):
        """public abstract java.lang.Object dev.ultreon.libs.functions.v0.misc.Method.call(T,java.lang.Object...)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ThrowingSupplier
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.misc.ThrowingSupplier as __ThrowingSupplier
__ThrowingSupplier = __ThrowingSupplier
 
class ThrowingSupplier(ABC):
    """dev.ultreon.libs.functions.v0.misc.ThrowingSupplier"""
 
    @staticmethod
    def __wrap(java_value: __ThrowingSupplier) -> 'ThrowingSupplier':
        return ThrowingSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThrowingSupplier):
        """
        Dynamic initializer for ThrowingSupplier.
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
    def get(self, ):
        """public abstract T dev.ultreon.libs.functions.v0.misc.ThrowingSupplier.get() throws E"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.Mapper
import dev.ultreon.libs.functions.v0.misc.Mapper as __Mapper
__Mapper = __Mapper
from abc import abstractmethod, ABC
 
class Mapper(ABC):
    """dev.ultreon.libs.functions.v0.misc.Mapper"""
 
    @staticmethod
    def __wrap(java_value: __Mapper) -> 'Mapper':
        return Mapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Mapper):
        """
        Dynamic initializer for Mapper.
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
    def map(self, arg0: object):
        """public abstract B dev.ultreon.libs.functions.v0.misc.Mapper.map(A)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable
import dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable as __ParameterizedRunnable
__ParameterizedRunnable = __ParameterizedRunnable
from abc import abstractmethod, ABC
 
class ParameterizedRunnable(ABC):
    """dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable"""
 
    @staticmethod
    def __wrap(java_value: __ParameterizedRunnable) -> 'ParameterizedRunnable':
        return ParameterizedRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ParameterizedRunnable):
        """
        Dynamic initializer for ParameterizedRunnable.
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
    def run(self, arg0: object):
        """public abstract void dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable.run(T)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ThrowingConsumer
import dev.ultreon.libs.functions.v0.misc.ThrowingConsumer as __ThrowingConsumer
__ThrowingConsumer = __ThrowingConsumer
from abc import abstractmethod, ABC
 
class ThrowingConsumer(ABC):
    """dev.ultreon.libs.functions.v0.misc.ThrowingConsumer"""
 
    @staticmethod
    def __wrap(java_value: __ThrowingConsumer) -> 'ThrowingConsumer':
        return ThrowingConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ThrowingConsumer):
        """
        Dynamic initializer for ThrowingConsumer.
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
    def accept(self, arg0: object):
        """public abstract void dev.ultreon.libs.functions.v0.misc.ThrowingConsumer.accept(T) throws E"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.Applier
import dev.ultreon.libs.functions.v0.misc.Applier as __Applier
__Applier = __Applier
from abc import abstractmethod, ABC
 
class Applier(ABC):
    """dev.ultreon.libs.functions.v0.misc.Applier"""
 
    @staticmethod
    def __wrap(java_value: __Applier) -> 'Applier':
        return Applier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Applier):
        """
        Dynamic initializer for Applier.
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
    def apply(self, arg0: object):
        """public abstract R dev.ultreon.libs.functions.v0.misc.Applier.apply(T)"""
        pass