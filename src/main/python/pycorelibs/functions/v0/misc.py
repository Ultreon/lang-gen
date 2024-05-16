from __future__ import annotations
from overload import overload


 
import dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable as _ParameterizedRunnable
_ParameterizedRunnable = _ParameterizedRunnable
from abc import abstractmethod, ABC
 
class ParameterizedRunnable():
    """dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable"""
 
    @staticmethod
    def _wrap(java_value: _ParameterizedRunnable) -> 'ParameterizedRunnable':
        return ParameterizedRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParameterizedRunnable):
        """
        Dynamic initializer for ParameterizedRunnable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParameterizedRunnable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParameterizedRunnable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def run(self, arg0: object):
        """public abstract void dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable.run(T)"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable
import dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable as _ParameterizedRunnable
_ParameterizedRunnable = _ParameterizedRunnable
from abc import abstractmethod, ABC
 
class ParameterizedRunnable():
    """dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable"""
 
    @staticmethod
    def _wrap(java_value: _ParameterizedRunnable) -> 'ParameterizedRunnable':
        return ParameterizedRunnable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ParameterizedRunnable):
        """
        Dynamic initializer for ParameterizedRunnable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ParameterizedRunnable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ParameterizedRunnable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def run(self, arg0: object):
        """public abstract void dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable.run(T)"""
        pass

 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ParameterizedRunnable 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.Mapper
import dev.ultreon.libs.functions.v0.misc.Mapper as _Mapper
_Mapper = _Mapper
from abc import abstractmethod, ABC
 
class Mapper():
    """dev.ultreon.libs.functions.v0.misc.Mapper"""
 
    @staticmethod
    def _wrap(java_value: _Mapper) -> 'Mapper':
        return Mapper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Mapper):
        """
        Dynamic initializer for Mapper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Mapper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Mapper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def map(self, arg0: object):
        """public abstract B dev.ultreon.libs.functions.v0.misc.Mapper.map(A)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.Method
from builtins import object
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.misc.Method as _Method
_Method = _Method
 
class Method():
    """dev.ultreon.libs.functions.v0.misc.Method"""
 
    @staticmethod
    def _wrap(java_value: _Method) -> 'Method':
        return Method(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Method):
        """
        Dynamic initializer for Method.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Method__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Method__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def call(self, arg0: object, *arg1: object):
        """public abstract java.lang.Object dev.ultreon.libs.functions.v0.misc.Method.call(T,java.lang.Object...)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ThrowingFunction
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.misc.ThrowingFunction as _ThrowingFunction
_ThrowingFunction = _ThrowingFunction
 
class ThrowingFunction():
    """dev.ultreon.libs.functions.v0.misc.ThrowingFunction"""
 
    @staticmethod
    def _wrap(java_value: _ThrowingFunction) -> 'ThrowingFunction':
        return ThrowingFunction(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThrowingFunction):
        """
        Dynamic initializer for ThrowingFunction.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThrowingFunction__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThrowingFunction__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, arg0: object):
        """public abstract R dev.ultreon.libs.functions.v0.misc.ThrowingFunction.apply(T) throws E"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.Applier
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.misc.Applier as _Applier
_Applier = _Applier
 
class Applier():
    """dev.ultreon.libs.functions.v0.misc.Applier"""
 
    @staticmethod
    def _wrap(java_value: _Applier) -> 'Applier':
        return Applier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Applier):
        """
        Dynamic initializer for Applier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Applier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Applier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def apply(self, arg0: object):
        """public abstract R dev.ultreon.libs.functions.v0.misc.Applier.apply(T)"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ThrowingSupplier
from abc import abstractmethod, ABC
import dev.ultreon.libs.functions.v0.misc.ThrowingSupplier as _ThrowingSupplier
_ThrowingSupplier = _ThrowingSupplier
 
class ThrowingSupplier():
    """dev.ultreon.libs.functions.v0.misc.ThrowingSupplier"""
 
    @staticmethod
    def _wrap(java_value: _ThrowingSupplier) -> 'ThrowingSupplier':
        return ThrowingSupplier(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThrowingSupplier):
        """
        Dynamic initializer for ThrowingSupplier.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThrowingSupplier__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThrowingSupplier__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def get(self, ):
        """public abstract T dev.ultreon.libs.functions.v0.misc.ThrowingSupplier.get() throws E"""
        pass 
 
 
# CLASS: dev.ultreon.libs.functions.v0.misc.ThrowingConsumer
import dev.ultreon.libs.functions.v0.misc.ThrowingConsumer as _ThrowingConsumer
_ThrowingConsumer = _ThrowingConsumer
from abc import abstractmethod, ABC
 
class ThrowingConsumer():
    """dev.ultreon.libs.functions.v0.misc.ThrowingConsumer"""
 
    @staticmethod
    def _wrap(java_value: _ThrowingConsumer) -> 'ThrowingConsumer':
        return ThrowingConsumer(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ThrowingConsumer):
        """
        Dynamic initializer for ThrowingConsumer.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ThrowingConsumer__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ThrowingConsumer__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def accept(self, arg0: object):
        """public abstract void dev.ultreon.libs.functions.v0.misc.ThrowingConsumer.accept(T) throws E"""
        pass