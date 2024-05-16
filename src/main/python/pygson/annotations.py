from __future__ import annotations
from overload import overload


 
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import com.google.gson.annotations.Expose as __Expose
__Expose = __Expose
from abc import abstractmethod, ABC
 
class Expose(ABC, __Annotation, Annotation):
    """com.google.gson.annotations.Expose"""
 
    @staticmethod
    def __wrap(java_value: __Expose) -> 'Expose':
        return Expose(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Expose):
        """
        Dynamic initializer for Expose.
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
    def serialize(self, ):
        """public abstract boolean com.google.gson.annotations.Expose.serialize()"""
        pass

    @abstractmethod
    def deserialize(self, ):
        """public abstract boolean com.google.gson.annotations.Expose.deserialize()"""
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

 
 
 
# CLASS: com.google.gson.annotations.Expose
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import com.google.gson.annotations.Expose as __Expose
__Expose = __Expose
from abc import abstractmethod, ABC
 
class Expose(ABC, __Annotation, Annotation):
    """com.google.gson.annotations.Expose"""
 
    @staticmethod
    def __wrap(java_value: __Expose) -> 'Expose':
        return Expose(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Expose):
        """
        Dynamic initializer for Expose.
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
    def serialize(self, ):
        """public abstract boolean com.google.gson.annotations.Expose.serialize()"""
        pass

    @abstractmethod
    def deserialize(self, ):
        """public abstract boolean com.google.gson.annotations.Expose.deserialize()"""
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

 
 
 
# CLASS: com.google.gson.annotations.Expose 
 
 
# CLASS: com.google.gson.annotations.Until
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import com.google.gson.annotations.Until as __Until
__Until = __Until
from abc import abstractmethod, ABC
 
class Until(ABC, __Annotation, Annotation):
    """com.google.gson.annotations.Until"""
 
    @staticmethod
    def __wrap(java_value: __Until) -> 'Until':
        return Until(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Until):
        """
        Dynamic initializer for Until.
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
    def value(self, ):
        """public abstract double com.google.gson.annotations.Until.value()"""
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
 
 
# CLASS: com.google.gson.annotations.Since
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import com.google.gson.annotations.Since as __Since
__Since = __Since
from abc import abstractmethod, ABC
 
class Since(ABC, __Annotation, Annotation):
    """com.google.gson.annotations.Since"""
 
    @staticmethod
    def __wrap(java_value: __Since) -> 'Since':
        return Since(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Since):
        """
        Dynamic initializer for Since.
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
    def value(self, ):
        """public abstract double com.google.gson.annotations.Since.value()"""
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
 
 
# CLASS: com.google.gson.annotations.JsonAdapter
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
import com.google.gson.annotations.JsonAdapter as __JsonAdapter
__JsonAdapter = __JsonAdapter
from abc import abstractmethod, ABC
 
class JsonAdapter(ABC, __Annotation, Annotation):
    """com.google.gson.annotations.JsonAdapter"""
 
    @staticmethod
    def __wrap(java_value: __JsonAdapter) -> 'JsonAdapter':
        return JsonAdapter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __JsonAdapter):
        """
        Dynamic initializer for JsonAdapter.
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
    def nullSafe(self, ):
        """public abstract boolean com.google.gson.annotations.JsonAdapter.nullSafe()"""
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
    def value(self, ):
        """public abstract java.lang.Class<?> com.google.gson.annotations.JsonAdapter.value()"""
        pass

    @abstractmethod
    def annotationType(self, ):
        """public abstract java.lang.Class<? extends java.lang.annotation.Annotation> java.lang.annotation.Annotation.annotationType()"""
        pass 
 
 
# CLASS: com.google.gson.annotations.SerializedName
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from abc import abstractmethod, ABC
import com.google.gson.annotations.SerializedName as __SerializedName
__SerializedName = __SerializedName
 
class SerializedName(ABC, __Annotation, Annotation):
    """com.google.gson.annotations.SerializedName"""
 
    @staticmethod
    def __wrap(java_value: __SerializedName) -> 'SerializedName':
        return SerializedName(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __SerializedName):
        """
        Dynamic initializer for SerializedName.
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
    def alternate(self, ):
        """public abstract java.lang.String[] com.google.gson.annotations.SerializedName.alternate()"""
        pass

    @abstractmethod
    def value(self, ):
        """public abstract java.lang.String com.google.gson.annotations.SerializedName.value()"""
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