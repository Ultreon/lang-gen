from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.gamerule.Rule as __Rule
__Rule = __Rule
from abc import abstractmethod, ABC
 
class Rule(ABC):
    """dev.ultreon.quantum.gamerule.Rule"""
 
    @staticmethod
    def __wrap(java_value: __Rule) -> 'Rule':
        return Rule(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rule):
        """
        Dynamic initializer for Rule.
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
    def getStringValue(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.gamerule.Rule.getStringValue()"""
        pass

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract void dev.ultreon.quantum.gamerule.Rule.setValue(T)"""
        pass

    @abstractmethod
    def getDefault(self, ):
        """public abstract T dev.ultreon.quantum.gamerule.Rule.getDefault()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.gamerule.Rule.getKey()"""
        pass

    @overload
    def reset(self):
        """public default void dev.ultreon.quantum.gamerule.Rule.reset()"""
        super(Rule, self).reset()

    @abstractmethod
    def getValue(self, ):
        """public abstract T dev.ultreon.quantum.gamerule.Rule.getValue()"""
        pass

    @abstractmethod
    def setStringValue(self, arg0: str):
        """public abstract void dev.ultreon.quantum.gamerule.Rule.setStringValue(java.lang.String) throws dev.ultreon.quantum.api.commands.CommandExecuteException"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.gamerule.Rule
import dev.ultreon.quantum.gamerule.Rule as __Rule
__Rule = __Rule
from abc import abstractmethod, ABC
 
class Rule(ABC):
    """dev.ultreon.quantum.gamerule.Rule"""
 
    @staticmethod
    def __wrap(java_value: __Rule) -> 'Rule':
        return Rule(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Rule):
        """
        Dynamic initializer for Rule.
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
    def getStringValue(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.gamerule.Rule.getStringValue()"""
        pass

    @abstractmethod
    def setValue(self, arg0: object):
        """public abstract void dev.ultreon.quantum.gamerule.Rule.setValue(T)"""
        pass

    @abstractmethod
    def getDefault(self, ):
        """public abstract T dev.ultreon.quantum.gamerule.Rule.getDefault()"""
        pass

    @abstractmethod
    def getKey(self, ):
        """public abstract java.lang.String dev.ultreon.quantum.gamerule.Rule.getKey()"""
        pass

    @overload
    def reset(self):
        """public default void dev.ultreon.quantum.gamerule.Rule.reset()"""
        super(Rule, self).reset()

    @abstractmethod
    def getValue(self, ):
        """public abstract T dev.ultreon.quantum.gamerule.Rule.getValue()"""
        pass

    @abstractmethod
    def setStringValue(self, arg0: str):
        """public abstract void dev.ultreon.quantum.gamerule.Rule.setStringValue(java.lang.String) throws dev.ultreon.quantum.api.commands.CommandExecuteException"""
        pass

 
 
 
# CLASS: dev.ultreon.quantum.gamerule.Rule 
 
 
# CLASS: dev.ultreon.quantum.gamerule.GameRules
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import dev.ultreon.quantum.gamerule.Rule as __Rule
__Rule = __Rule
import java.lang.Enum as Enum
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import dev.ultreon.quantum.gamerule.GameRules as __GameRules
__GameRules = __GameRules
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Double as __double
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class GameRules():
    """dev.ultreon.quantum.gamerule.GameRules"""
 
    @staticmethod
    def __wrap(java_value: __GameRules) -> 'GameRules':
        return GameRules(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __GameRules):
        """
        Dynamic initializer for GameRules.
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
    def enumRule(self, arg0: str, arg1: 'Enum') -> 'Rule':
        """public <T extends java.lang.Enum<T>> dev.ultreon.quantum.gamerule.Rule<T> dev.ultreon.quantum.gamerule.GameRules.enumRule(java.lang.String,T)"""
        return 'Rule'.__wrap(super(__GameRules, self).enumRule(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public dev.ultreon.quantum.gamerule.GameRules()"""
        val = __GameRules()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def numberRule(self, arg0: str, arg1: float) -> 'Rule':
        """public dev.ultreon.quantum.gamerule.Rule<java.lang.Double> dev.ultreon.quantum.gamerule.GameRules.numberRule(java.lang.String,double)"""
        return 'Rule'.__wrap(super(__GameRules, self).numberRule(arg0, __double.valueOf(arg1)))

    @overload
    def booleanRule(self, arg0: str, arg1: bool) -> 'Rule':
        """public dev.ultreon.quantum.gamerule.Rule<java.lang.Boolean> dev.ultreon.quantum.gamerule.GameRules.booleanRule(java.lang.String,boolean)"""
        return 'Rule'.__wrap(super(__GameRules, self).booleanRule(arg0, __boolean.valueOf(arg1)))

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
    def __init__(self):
        """public dev.ultreon.quantum.gamerule.GameRules()"""
        val = __GameRules()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def getRules(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.gamerule.Rule<?>> dev.ultreon.quantum.gamerule.GameRules.getRules()"""
        return 'List'.__wrap(super(GameRules, self).getRules())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def getRule(self, arg0: str) -> 'Rule':
        """public dev.ultreon.quantum.gamerule.Rule<?> dev.ultreon.quantum.gamerule.GameRules.getRule(java.lang.String)"""
        return 'Rule'.__wrap(super(__GameRules, self).getRule(arg0))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))