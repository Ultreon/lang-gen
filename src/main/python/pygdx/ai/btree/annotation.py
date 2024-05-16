from __future__ import annotations
from overload import overload


 
import com.badlogic.gdx.ai.btree.annotation.TaskAttribute as _TaskAttribute
_TaskAttribute = _TaskAttribute
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class TaskAttribute():
    """com.badlogic.gdx.ai.btree.annotation.TaskAttribute"""
 
    @staticmethod
    def _wrap(java_value: _TaskAttribute) -> 'TaskAttribute':
        return TaskAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TaskAttribute):
        """
        Dynamic initializer for TaskAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TaskAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TaskAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def required(self, ):
        """public abstract boolean com.badlogic.gdx.ai.btree.annotation.TaskAttribute.required()"""
        pass

    @abstractmethod
    def name(self, ):
        """public abstract java.lang.String com.badlogic.gdx.ai.btree.annotation.TaskAttribute.name()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.annotation.TaskAttribute
import com.badlogic.gdx.ai.btree.annotation.TaskAttribute as _TaskAttribute
_TaskAttribute = _TaskAttribute
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class TaskAttribute():
    """com.badlogic.gdx.ai.btree.annotation.TaskAttribute"""
 
    @staticmethod
    def _wrap(java_value: _TaskAttribute) -> 'TaskAttribute':
        return TaskAttribute(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TaskAttribute):
        """
        Dynamic initializer for TaskAttribute.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TaskAttribute__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TaskAttribute__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def required(self, ):
        """public abstract boolean com.badlogic.gdx.ai.btree.annotation.TaskAttribute.required()"""
        pass

    @abstractmethod
    def name(self, ):
        """public abstract java.lang.String com.badlogic.gdx.ai.btree.annotation.TaskAttribute.name()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass

 
 
 
# CLASS: com.badlogic.gdx.ai.btree.annotation.TaskAttribute 
 
 
# CLASS: com.badlogic.gdx.ai.btree.annotation.TaskConstraint
import com.badlogic.gdx.ai.btree.annotation.TaskConstraint as _TaskConstraint
_TaskConstraint = _TaskConstraint
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class TaskConstraint():
    """com.badlogic.gdx.ai.btree.annotation.TaskConstraint"""
 
    @staticmethod
    def _wrap(java_value: _TaskConstraint) -> 'TaskConstraint':
        return TaskConstraint(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TaskConstraint):
        """
        Dynamic initializer for TaskConstraint.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TaskConstraint__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TaskConstraint__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def maxChildren(self, ):
        """public abstract int com.badlogic.gdx.ai.btree.annotation.TaskConstraint.maxChildren()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.lang.annotation.Annotation.equals(java.lang.Object)"""
        pass

    @abstractmethod
    def toString(self, ):
        """public abstract java.lang.String java.lang.annotation.Annotation.toString()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.lang.annotation.Annotation.hashCode()"""
        pass

    @abstractmethod
    def minChildren(self, ):
        """public abstract int com.badlogic.gdx.ai.btree.annotation.TaskConstraint.minChildren()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass