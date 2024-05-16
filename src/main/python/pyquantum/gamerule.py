from __future__ import annotations
from overload import overload


 
import dev.ultreon.quantum.gamerule.Rule as _Rule
_Rule = _Rule
from abc import abstractmethod, ABC
 
class Rule():
    """dev.ultreon.quantum.gamerule.Rule"""
 
    @staticmethod
    def _wrap(java_value: _Rule) -> 'Rule':
        return Rule(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rule):
        """
        Dynamic initializer for Rule.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rule__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rule__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import dev.ultreon.quantum.gamerule.Rule as _Rule
_Rule = _Rule
from abc import abstractmethod, ABC
 
class Rule():
    """dev.ultreon.quantum.gamerule.Rule"""
 
    @staticmethod
    def _wrap(java_value: _Rule) -> 'Rule':
        return Rule(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Rule):
        """
        Dynamic initializer for Rule.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Rule__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Rule__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
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
import java.lang.Double as _double
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import dev.ultreon.quantum.gamerule.GameRules as _GameRules
_GameRules = _GameRules
import dev.ultreon.quantum.gamerule.Rule as _Rule
_Rule = _Rule
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import java.lang.Enum as Enum
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class GameRules():
    """dev.ultreon.quantum.gamerule.GameRules"""
 
    @staticmethod
    def _wrap(java_value: _GameRules) -> 'GameRules':
        return GameRules(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _GameRules):
        """
        Dynamic initializer for GameRules.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_GameRules__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_GameRules__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def booleanRule(self, arg0: str, arg1: bool) -> 'Rule':
        """public dev.ultreon.quantum.gamerule.Rule<java.lang.Boolean> dev.ultreon.quantum.gamerule.GameRules.booleanRule(java.lang.String,boolean)"""
        return 'Rule'._wrap(super(_GameRules, self).booleanRule(arg0, _boolean.valueOf(arg1)))

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
    def getRules(self) -> 'List':
        """public java.util.List<dev.ultreon.quantum.gamerule.Rule<?>> dev.ultreon.quantum.gamerule.GameRules.getRules()"""
        return 'List'._wrap(super(GameRules, self).getRules())

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
    def __init__(self, ):
        """public dev.ultreon.quantum.gamerule.GameRules()"""
        val = _GameRules()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRule(self, arg0: str) -> 'Rule':
        """public dev.ultreon.quantum.gamerule.Rule<?> dev.ultreon.quantum.gamerule.GameRules.getRule(java.lang.String)"""
        return 'Rule'._wrap(super(_GameRules, self).getRule(arg0))

    @overload
    def enumRule(self, arg0: str, arg1: 'Enum') -> 'Rule':
        """public <T extends java.lang.Enum<T>> dev.ultreon.quantum.gamerule.Rule<T> dev.ultreon.quantum.gamerule.GameRules.enumRule(java.lang.String,T)"""
        return 'Rule'._wrap(super(_GameRules, self).enumRule(arg0, arg1))

    @overload
    def numberRule(self, arg0: str, arg1: float) -> 'Rule':
        """public dev.ultreon.quantum.gamerule.Rule<java.lang.Double> dev.ultreon.quantum.gamerule.GameRules.numberRule(java.lang.String,double)"""
        return 'Rule'._wrap(super(_GameRules, self).numberRule(arg0, _double.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public dev.ultreon.quantum.gamerule.GameRules()"""
        val = _GameRules()
        self.__wrapper = val