from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Character as _char
import java.lang.Double as _double
import org.apache.commons.lang3.builder.DiffResult as _DiffResult
_DiffResult = _DiffResult
from pyquantum_helper import override
import org.apache.commons.lang3.builder.DiffBuilder as _DiffBuilder
_DiffBuilder = _DiffBuilder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DiffBuilder():
    """org.apache.commons.lang3.builder.DiffBuilder"""
 
    @staticmethod
    def _wrap(java_value: _DiffBuilder) -> 'DiffBuilder':
        return DiffBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DiffBuilder):
        """
        Dynamic initializer for DiffBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DiffBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DiffBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def append(self, arg0: str, arg1: 'Object', arg2: 'Object') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,java.lang.Object[],java.lang.Object[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: 'short', arg2: 'short') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,short[],short[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: str, arg1: float, arg2: float) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,float,float)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,int,int)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'char', arg2: 'char') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,char[],char[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

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

    @overload
    def append(self, arg0: str, arg1: bool, arg2: bool) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,boolean,boolean)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: float, arg2: float) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,double,double)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'float', arg2: 'float') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,float[],float[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: 'boolean', arg2: 'boolean') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,boolean[],boolean[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def append(self, arg0: str, arg1: str, arg2: str) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,char,char)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _char.valueOf(arg1), _char.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,short,short)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _short.valueOf(arg1), _short.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,byte,byte)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _byte.valueOf(arg1), _byte.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle', arg3: bool):
        """public org.apache.commons.lang3.builder.DiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        val = _DiffBuilder(arg0, arg1, arg2, _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def build(self) -> 'DiffResult':
        """public org.apache.commons.lang3.builder.DiffResult<T> org.apache.commons.lang3.builder.DiffBuilder.build()"""
        return 'DiffResult'._wrap(super(DiffBuilder, self).build())

    @overload
    def append(self, arg0: str, arg1: 'long', arg2: 'long') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,long[],long[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: object, arg2: object) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: bytes, arg2: bytes) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,byte[],byte[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, bytes, bytes))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,long,long)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _long.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'DiffResult') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,org.apache.commons.lang3.builder.DiffResult<T>)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: 'double', arg2: 'double') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,double[],double[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.DiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = _DiffBuilder(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: str, arg1: 'int', arg2: 'int') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,int[],int[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffBuilder
from builtins import str
import java.lang.Character as _char
import java.lang.Double as _double
import org.apache.commons.lang3.builder.DiffResult as _DiffResult
_DiffResult = _DiffResult
from pyquantum_helper import override
import org.apache.commons.lang3.builder.DiffBuilder as _DiffBuilder
_DiffBuilder = _DiffBuilder
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class DiffBuilder():
    """org.apache.commons.lang3.builder.DiffBuilder"""
 
    @staticmethod
    def _wrap(java_value: _DiffBuilder) -> 'DiffBuilder':
        return DiffBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DiffBuilder):
        """
        Dynamic initializer for DiffBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DiffBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DiffBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def append(self, arg0: str, arg1: 'Object', arg2: 'Object') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,java.lang.Object[],java.lang.Object[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: 'short', arg2: 'short') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,short[],short[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: str, arg1: float, arg2: float) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,float,float)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _float.valueOf(arg1), _float.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,int,int)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _int.valueOf(arg1), _int.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'char', arg2: 'char') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,char[],char[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

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

    @overload
    def append(self, arg0: str, arg1: bool, arg2: bool) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,boolean,boolean)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _boolean.valueOf(arg1), _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: float, arg2: float) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,double,double)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _double.valueOf(arg1), _double.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'float', arg2: 'float') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,float[],float[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: 'boolean', arg2: 'boolean') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,boolean[],boolean[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def append(self, arg0: str, arg1: str, arg2: str) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,char,char)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _char.valueOf(arg1), _char.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,short,short)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _short.valueOf(arg1), _short.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,byte,byte)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _byte.valueOf(arg1), _byte.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle', arg3: bool):
        """public org.apache.commons.lang3.builder.DiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        val = _DiffBuilder(arg0, arg1, arg2, _boolean.valueOf(arg3))
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def build(self) -> 'DiffResult':
        """public org.apache.commons.lang3.builder.DiffResult<T> org.apache.commons.lang3.builder.DiffBuilder.build()"""
        return 'DiffResult'._wrap(super(DiffBuilder, self).build())

    @overload
    def append(self, arg0: str, arg1: 'long', arg2: 'long') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,long[],long[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: object, arg2: object) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,java.lang.Object,java.lang.Object)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @overload
    def append(self, arg0: str, arg1: bytes, arg2: bytes) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,byte[],byte[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, bytes, bytes))

    @overload
    def append(self, arg0: str, arg1: int, arg2: int) -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,long,long)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, _long.valueOf(arg1), _long.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'DiffResult') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,org.apache.commons.lang3.builder.DiffResult<T>)"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: 'double', arg2: 'double') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,double[],double[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.DiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = _DiffBuilder(arg0, arg1, arg2)
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: str, arg1: 'int', arg2: 'int') -> 'DiffBuilder':
        """public org.apache.commons.lang3.builder.DiffBuilder<T> org.apache.commons.lang3.builder.DiffBuilder.append(java.lang.String,int[],int[])"""
        return 'DiffBuilder'._wrap(super(_DiffBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffBuilder 
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringExclude
import org.apache.commons.lang3.builder.ToStringExclude as _ToStringExclude
_ToStringExclude = _ToStringExclude
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class ToStringExclude():
    """org.apache.commons.lang3.builder.ToStringExclude"""
 
    @staticmethod
    def _wrap(java_value: _ToStringExclude) -> 'ToStringExclude':
        return ToStringExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToStringExclude):
        """
        Dynamic initializer for ToStringExclude.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToStringExclude__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToStringExclude__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringSummary
import org.apache.commons.lang3.builder.ToStringSummary as _ToStringSummary
_ToStringSummary = _ToStringSummary
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class ToStringSummary():
    """org.apache.commons.lang3.builder.ToStringSummary"""
 
    @staticmethod
    def _wrap(java_value: _ToStringSummary) -> 'ToStringSummary':
        return ToStringSummary(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToStringSummary):
        """
        Dynamic initializer for ToStringSummary.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToStringSummary__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToStringSummary__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
 
 
# CLASS: org.apache.commons.lang3.builder.Diff
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
try:
    from pyapache.lang3 import tuple
except ImportError:
    tuple = _import_once("pyapache.lang3.tuple")

from builtins import type
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
from builtins import object
from abc import abstractmethod, ABC
import java.lang.reflect.Type as _Type
_Type = _Type
from typing import List
import java.lang.String as _string
import java.util.Map.Entry as Entry
import java.lang.Integer as _int
import org.apache.commons.lang3.tuple.Pair as _Pair
_Pair = _Pair
try:
    from pyapache.lang3 import function
except ImportError:
    function = _import_once("pyapache.lang3.function")

from builtins import bool
import java.lang.Long as _long
import org.apache.commons.lang3.builder.Diff as _Diff
_Diff = _Diff
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Diff():
    """org.apache.commons.lang3.builder.Diff"""
 
    @staticmethod
    def _wrap(java_value: _Diff) -> 'Diff':
        return Diff(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Diff):
        """
        Dynamic initializer for Diff.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Diff__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Diff__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.tuple.Pair.hashCode()"""
        return int._wrap(super(tuple.Pair, self).hashCode())

    @overload
    def toString(self, arg0: str) -> str:
        """public java.lang.String org.apache.commons.lang3.tuple.Pair.toString(java.lang.String)"""
        return str._wrap(super(_tuple.Pair, self).toString(arg0))

    @staticmethod
    @overload
    def ofNonNull(arg0: object, arg1: object) -> 'tuple.Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.ofNonNull(L,R)"""
        return tuple.Pair._wrap(_Pair.ofNonNull(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def emptyArray() -> List['tuple.Pair']:
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R>[] org.apache.commons.lang3.tuple.Pair.emptyArray()"""
        return List[tuple.Pair]._wrap(_Pair.emptyArray())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getFieldName(self) -> str:
        """public final java.lang.String org.apache.commons.lang3.builder.Diff.getFieldName()"""
        return str._wrap(super(Diff, self).getFieldName())

    @staticmethod
    @overload
    def of(arg0: 'Entry') -> 'tuple.Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(java.util.Map$Entry<L, R>)"""
        return tuple.Pair._wrap(_Pair.of(arg0))

    @abstractmethod
    def getRight(self, ):
        """public abstract R org.apache.commons.lang3.tuple.Pair.getRight()"""
        pass

    @override
    @overload
    def accept(self, arg0: 'FailableBiConsumer'):
        """public <E extends java.lang.Throwable> void org.apache.commons.lang3.tuple.Pair.accept(org.apache.commons.lang3.function.FailableBiConsumer<L, R, E>) throws E"""
        super(_tuple.Pair, self).accept(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.tuple.Pair.equals(java.lang.Object)"""
        return bool._wrap(super(_tuple.Pair, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def of(arg0: object, arg1: object) -> 'tuple.Pair':
        """public static <L,R> org.apache.commons.lang3.tuple.Pair<L, R> org.apache.commons.lang3.tuple.Pair.of(L,R)"""
        return tuple.Pair._wrap(_Pair.of(arg0, arg1))

    @overload
    def compareTo(self, arg0: 'Pair') -> int:
        """public int org.apache.commons.lang3.tuple.Pair.compareTo(org.apache.commons.lang3.tuple.Pair<L, R>)"""
        return int._wrap(super(_tuple.Pair, self).compareTo(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @abstractmethod
    def getLeft(self, ):
        """public abstract L org.apache.commons.lang3.tuple.Pair.getLeft()"""
        pass

    @overload
    def setValue(self, arg0: object) -> object:
        """public final T org.apache.commons.lang3.builder.Diff.setValue(T)"""
        return object._wrap(super(_Diff, self).setValue(arg0))

    @override
    @overload
    def getValue(self) -> object:
        """public R org.apache.commons.lang3.tuple.Pair.getValue()"""
        return object._wrap(super(tuple.Pair, self).getValue())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def apply(self, arg0: 'FailableBiFunction') -> object:
        """public <V,E extends java.lang.Throwable> V org.apache.commons.lang3.tuple.Pair.apply(org.apache.commons.lang3.function.FailableBiFunction<L, R, V, E>) throws E"""
        return object._wrap(super(_tuple.Pair, self).apply(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type org.apache.commons.lang3.builder.Diff.getType()"""
        return 'Type'._wrap(super(Diff, self).getType())

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String org.apache.commons.lang3.builder.Diff.toString()"""
        return str._wrap(super(Diff, self).toString())

    @override
    @overload
    def getKey(self) -> object:
        """public final L org.apache.commons.lang3.tuple.Pair.getKey()"""
        return object._wrap(super(tuple.Pair, self).getKey()) 
 
 
# CLASS: org.apache.commons.lang3.builder.ReflectionToStringBuilder
import java.lang.Double as _double
import java.lang.Character as _char
import java.lang.StringBuffer as _StringBuffer
_StringBuffer = _StringBuffer
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Collection as Collection
import java.lang.Short as _short
import org.apache.commons.lang3.builder.ReflectionToStringBuilder as _ReflectionToStringBuilder
_ReflectionToStringBuilder = _ReflectionToStringBuilder
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
from builtins import bool
from builtins import str
import org.apache.commons.lang3.builder.ToStringStyle as _ToStringStyle
_ToStringStyle = _ToStringStyle
from pyquantum_helper import override
import java.lang.Object as _object
import org.apache.commons.lang3.builder.ToStringBuilder as _ToStringBuilder
_ToStringBuilder = _ToStringBuilder
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Float as _float
import java.lang.Integer as _int
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ReflectionToStringBuilder():
    """org.apache.commons.lang3.builder.ReflectionToStringBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ReflectionToStringBuilder) -> 'ReflectionToStringBuilder':
        return ReflectionToStringBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectionToStringBuilder):
        """
        Dynamic initializer for ReflectionToStringBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectionToStringBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectionToStringBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def append(self, arg0: str, arg1: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, bytes))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        return str._wrap(_ReflectionToStringBuilder.toString(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @override
    @overload
    def getStyle(self) -> 'ToStringStyle':
        """public org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getStyle()"""
        return 'ToStringStyle'._wrap(super(ToStringBuilder, self).getStyle())

    @overload
    def append(self, arg0: str, arg1: 'boolean', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'long', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: bool, arg4: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,boolean,java.lang.Class<? super T>)"""
        return str._wrap(_ReflectionToStringBuilder.toString(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3), arg4))

    @overload
    def append(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: 'float', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _float.valueOf(arg1)))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def toStringInclude(arg0: object, arg1: 'Collection') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringInclude(java.lang.Object,java.util.Collection<java.lang.String>)"""
        return str._wrap(_ReflectionToStringBuilder.toStringInclude(arg0, arg1))

    @overload
    def isAppendTransients(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.ReflectionToStringBuilder.isAppendTransients()"""
        return bool._wrap(super(ReflectionToStringBuilder, self).isAppendTransients())

    @overload
    def append(self, arg0: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(bytes))

    @override
    @overload
    def build(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.build()"""
        return str._wrap(super(ToStringBuilder, self).build())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString()"""
        return str._wrap(super(ReflectionToStringBuilder, self).toString())

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer', arg3: 'Class', arg4: bool, arg5: bool):
        """public <T> org.apache.commons.lang3.builder.ReflectionToStringBuilder(T,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer,java.lang.Class<? super T>,boolean,boolean)"""
        val = _ReflectionToStringBuilder(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4), _boolean.valueOf(arg5))
        self.__wrapper = val

    @staticmethod
    @overload
    def toStringExclude(arg0: object, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringExclude(java.lang.Object,java.lang.String...)"""
        return str._wrap(_ReflectionToStringBuilder.toStringExclude(arg0, arg1))

    @staticmethod
    @overload
    def toString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object)"""
        return str._wrap(_ReflectionToStringBuilder.toString(arg0))

    @overload
    def append(self, arg0: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _double.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_double.valueOf(arg0)))

    @override
    @overload
    def getStringBuffer(self) -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.builder.ToStringBuilder.getStringBuffer()"""
        return 'StringBuffer'._wrap(super(ToStringBuilder, self).getStringBuffer())

    @overload
    def append(self, arg0: str, arg1: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def appendSuper(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendSuper(java.lang.String)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).appendSuper(arg0))

    @overload
    def setAppendStatics(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setAppendStatics(boolean)"""
        super(_ReflectionToStringBuilder, self).setAppendStatics(_boolean.valueOf(arg0))

    @staticmethod
    @overload
    def getDefaultStyle() -> 'ToStringStyle':
        """public static org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getDefaultStyle()"""
        return ToStringStyle._wrap(_ToStringBuilder.getDefaultStyle())

    @overload
    def append(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_char.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,java.lang.Class<? super T>)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0, arg1, _boolean.valueOf(arg2), arg3))

    @overload
    def setExcludeFieldNames(self, *arg0: str) -> 'ReflectionToStringBuilder':
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder org.apache.commons.lang3.builder.ReflectionToStringBuilder.setExcludeFieldNames(java.lang.String...)"""
        return 'ReflectionToStringBuilder'._wrap(super(_ReflectionToStringBuilder, self).setExcludeFieldNames(arg0))

    @overload
    def setExcludeNullValues(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setExcludeNullValues(boolean)"""
        super(_ReflectionToStringBuilder, self).setExcludeNullValues(_boolean.valueOf(arg0))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _long.valueOf(arg1)))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: bool, arg4: bool, arg5: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,boolean,boolean,java.lang.Class<? super T>)"""
        return str._wrap(_ReflectionToStringBuilder.toString(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3), _boolean.valueOf(arg4), arg5))

    @overload
    def append(self, arg0: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder(java.lang.Object)"""
        val = _ReflectionToStringBuilder(arg0)
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: bytes, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, bytes, _boolean.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def append(self, arg0: str, arg1: 'double', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_int.valueOf(arg0)))

    @overload
    def setAppendTransients(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setAppendTransients(boolean)"""
        super(_ReflectionToStringBuilder, self).setAppendTransients(_boolean.valueOf(arg0))

    @overload
    def isExcludeNullValues(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.ReflectionToStringBuilder.isExcludeNullValues()"""
        return bool._wrap(super(ReflectionToStringBuilder, self).isExcludeNullValues())

    @overload
    def setUpToClass(self, arg0: 'Class'):
        """public void org.apache.commons.lang3.builder.ReflectionToStringBuilder.setUpToClass(java.lang.Class<?>)"""
        super(_ReflectionToStringBuilder, self).setUpToClass(arg0)

    @overload
    def getExcludeFieldNames(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.builder.ReflectionToStringBuilder.getExcludeFieldNames()"""
        return List[str]._wrap(super(ReflectionToStringBuilder, self).getExcludeFieldNames())

    @overload
    def append(self, arg0: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer'):
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer)"""
        val = _ReflectionToStringBuilder(arg0, arg1, arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean,boolean)"""
        return str._wrap(_ReflectionToStringBuilder.toString(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @overload
    def setIncludeFieldNames(self, *arg0: str) -> 'ReflectionToStringBuilder':
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder org.apache.commons.lang3.builder.ReflectionToStringBuilder.setIncludeFieldNames(java.lang.String...)"""
        return 'ReflectionToStringBuilder'._wrap(super(_ReflectionToStringBuilder, self).setIncludeFieldNames(arg0))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _int.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'char', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def reflectionToString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0))

    @overload
    def append(self, arg0: str, arg1: object, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object,boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def reflectionAppendArray(self, arg0: object) -> 'ReflectionToStringBuilder':
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder org.apache.commons.lang3.builder.ReflectionToStringBuilder.reflectionAppendArray(java.lang.Object)"""
        return 'ReflectionToStringBuilder'._wrap(super(_ReflectionToStringBuilder, self).reflectionAppendArray(arg0))

    @overload
    def append(self, arg0: str, arg1: 'Object', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.ReflectionToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = _ReflectionToStringBuilder(arg0, arg1)
        self.__wrapper = val

    @overload
    def append(self, arg0: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _byte.valueOf(arg1)))

    @staticmethod
    @overload
    def toString(arg0: object, arg1: 'ToStringStyle') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        return str._wrap(_ReflectionToStringBuilder.toString(arg0, arg1))

    @staticmethod
    @overload
    def toStringExclude(arg0: object, arg1: 'Collection') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringExclude(java.lang.Object,java.util.Collection<java.lang.String>)"""
        return str._wrap(_ReflectionToStringBuilder.toStringExclude(arg0, arg1))

    @overload
    def appendAsObjectToString(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendAsObjectToString(java.lang.Object)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).appendAsObjectToString(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def append(self, arg0: str, arg1: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer', arg3: 'Class', arg4: bool, arg5: bool, arg6: bool):
        """public <T> org.apache.commons.lang3.builder.ReflectionToStringBuilder(T,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer,java.lang.Class<? super T>,boolean,boolean,boolean)"""
        val = _ReflectionToStringBuilder(arg0, arg1, arg2, arg3, _boolean.valueOf(arg4), _boolean.valueOf(arg5), _boolean.valueOf(arg6))
        self.__wrapper = val

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_short.valueOf(arg0)))

    @overload
    def append(self, arg0: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def getUpToClass(self) -> 'type.Class':
        """public java.lang.Class<?> org.apache.commons.lang3.builder.ReflectionToStringBuilder.getUpToClass()"""
        return 'type.Class'._wrap(super(ReflectionToStringBuilder, self).getUpToClass())

    @staticmethod
    @overload
    def toStringInclude(arg0: object, *arg1: str) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ReflectionToStringBuilder.toStringInclude(java.lang.Object,java.lang.String...)"""
        return str._wrap(_ReflectionToStringBuilder.toStringInclude(arg0, arg1))

    @override
    @overload
    def getObject(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.builder.ToStringBuilder.getObject()"""
        return object._wrap(super(ToStringBuilder, self).getObject())

    @overload
    def append(self, arg0: str, arg1: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _char.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def setDefaultStyle(arg0: 'ToStringStyle'):
        """public static void org.apache.commons.lang3.builder.ToStringBuilder.setDefaultStyle(org.apache.commons.lang3.builder.ToStringStyle)"""
        _ToStringBuilder.setDefaultStyle(arg0)

    @overload
    def isAppendStatics(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.ReflectionToStringBuilder.isAppendStatics()"""
        return bool._wrap(super(ReflectionToStringBuilder, self).isAppendStatics())

    @overload
    def append(self, arg0: str, arg1: 'int', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def getIncludeFieldNames(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.builder.ReflectionToStringBuilder.getIncludeFieldNames()"""
        return List[str]._wrap(super(ReflectionToStringBuilder, self).getIncludeFieldNames())

    @overload
    def append(self, arg0: str, arg1: 'short', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_long.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def appendToString(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendToString(java.lang.String)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).appendToString(arg0))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _short.valueOf(arg1))) 
 
 
# CLASS: org.apache.commons.lang3.builder.EqualsExclude
import org.apache.commons.lang3.builder.EqualsExclude as _EqualsExclude
_EqualsExclude = _EqualsExclude
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class EqualsExclude():
    """org.apache.commons.lang3.builder.EqualsExclude"""
 
    @staticmethod
    def _wrap(java_value: _EqualsExclude) -> 'EqualsExclude':
        return EqualsExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EqualsExclude):
        """
        Dynamic initializer for EqualsExclude.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EqualsExclude__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EqualsExclude__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
 
 
# CLASS: org.apache.commons.lang3.builder.Builder
import org.apache.commons.lang3.builder.Builder as _Builder
_Builder = _Builder
from abc import abstractmethod, ABC
 
class Builder():
    """org.apache.commons.lang3.builder.Builder"""
 
    @staticmethod
    def _wrap(java_value: _Builder) -> 'Builder':
        return Builder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Builder):
        """
        Dynamic initializer for Builder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Builder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Builder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def build(self, ):
        """public abstract T org.apache.commons.lang3.builder.Builder.build()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.HashCodeExclude
import org.apache.commons.lang3.builder.HashCodeExclude as _HashCodeExclude
_HashCodeExclude = _HashCodeExclude
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class HashCodeExclude():
    """org.apache.commons.lang3.builder.HashCodeExclude"""
 
    @staticmethod
    def _wrap(java_value: _HashCodeExclude) -> 'HashCodeExclude':
        return HashCodeExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashCodeExclude):
        """
        Dynamic initializer for HashCodeExclude.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashCodeExclude__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashCodeExclude__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringBuilder
from builtins import str
import java.lang.Double as _double
import java.lang.Character as _char
import org.apache.commons.lang3.builder.ToStringStyle as _ToStringStyle
_ToStringStyle = _ToStringStyle
import java.lang.StringBuffer as _StringBuffer
_StringBuffer = _StringBuffer
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import org.apache.commons.lang3.builder.ToStringBuilder as _ToStringBuilder
_ToStringBuilder = _ToStringBuilder
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ToStringBuilder():
    """org.apache.commons.lang3.builder.ToStringBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ToStringBuilder) -> 'ToStringBuilder':
        return ToStringBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToStringBuilder):
        """
        Dynamic initializer for ToStringBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToStringBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToStringBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.ToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = _ToStringBuilder(arg0, arg1)
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, bytes))

    @overload
    def append(self, arg0: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'boolean', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'long', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.Object)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle') -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_byte.valueOf(arg0)))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,boolean)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: 'float', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,float)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _float.valueOf(arg1)))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_float.valueOf(arg0)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def append(self, arg0: bytes) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(byte[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(bytes))

    @override
    @overload
    def build(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.build()"""
        return str._wrap(super(ToStringBuilder, self).build())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _double.valueOf(arg1)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def append(self, arg0: float) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_double.valueOf(arg0)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.toString()"""
        return str._wrap(super(ToStringBuilder, self).toString())

    @overload
    def append(self, arg0: str, arg1: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def appendSuper(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendSuper(java.lang.String)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).appendSuper(arg0))

    @overload
    def __init__(self, arg0: object, arg1: 'ToStringStyle', arg2: 'StringBuffer'):
        """public org.apache.commons.lang3.builder.ToStringBuilder(java.lang.Object,org.apache.commons.lang3.builder.ToStringStyle,java.lang.StringBuffer)"""
        val = _ToStringBuilder(arg0, arg1, arg2)
        self.__wrapper = val

    @staticmethod
    @overload
    def getDefaultStyle() -> 'ToStringStyle':
        """public static org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getDefaultStyle()"""
        return ToStringStyle._wrap(_ToStringBuilder.getDefaultStyle())

    @overload
    def append(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_char.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionToString(arg0: object, arg1: 'ToStringStyle', arg2: bool, arg3: 'Class') -> str:
        """public static <T> java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(T,org.apache.commons.lang3.builder.ToStringStyle,boolean,java.lang.Class<? super T>)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0, arg1, _boolean.valueOf(arg2), arg3))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _long.valueOf(arg1)))

    @overload
    def append(self, arg0: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: str, arg1: bytes, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, bytes, _boolean.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @overload
    def append(self, arg0: str, arg1: 'double', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_int.valueOf(arg0)))

    @overload
    def append(self, arg0: 'float') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(float[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(double[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def __init__(self, arg0: object):
        """public org.apache.commons.lang3.builder.ToStringBuilder(java.lang.Object)"""
        val = _ToStringBuilder(arg0)
        self.__wrapper = val

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _int.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'char', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def reflectionToString(arg0: object) -> str:
        """public static java.lang.String org.apache.commons.lang3.builder.ToStringBuilder.reflectionToString(java.lang.Object)"""
        return str._wrap(_ToStringBuilder.reflectionToString(arg0))

    @overload
    def append(self, arg0: str, arg1: object, arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object,boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'Object', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def getStringBuffer(self) -> 'StringBuffer':
        """public java.lang.StringBuffer org.apache.commons.lang3.builder.ToStringBuilder.getStringBuffer()"""
        return 'StringBuffer'._wrap(super(ToStringBuilder, self).getStringBuffer())

    @overload
    def append(self, arg0: str, arg1: 'short') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(boolean[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def append(self, arg0: str, arg1: 'Object') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,java.lang.Object[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,byte)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _byte.valueOf(arg1)))

    @overload
    def appendAsObjectToString(self, arg0: object) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendAsObjectToString(java.lang.Object)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).appendAsObjectToString(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def append(self, arg0: str, arg1: 'long') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,long[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(short)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_short.valueOf(arg0)))

    @overload
    def append(self, arg0: 'int') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(int[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def getStyle(self) -> 'ToStringStyle':
        """public org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.ToStringBuilder.getStyle()"""
        return 'ToStringStyle'._wrap(super(ToStringBuilder, self).getStyle())

    @overload
    def append(self, arg0: str, arg1: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,char)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _char.valueOf(arg1)))

    @overload
    def append(self, arg0: str, arg1: 'double') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,double[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def setDefaultStyle(arg0: 'ToStringStyle'):
        """public static void org.apache.commons.lang3.builder.ToStringBuilder.setDefaultStyle(org.apache.commons.lang3.builder.ToStringStyle)"""
        _ToStringBuilder.setDefaultStyle(arg0)

    @overload
    def append(self, arg0: str, arg1: 'int', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,int[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: 'short', arg2: bool) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short[],boolean)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(long)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(_long.valueOf(arg0)))

    @overload
    def append(self, arg0: str, arg1: 'boolean') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,boolean[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'char') -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(char[])"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0))

    @overload
    def appendToString(self, arg0: str) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.appendToString(java.lang.String)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).appendToString(arg0))

    @overload
    def append(self, arg0: str, arg1: int) -> 'ToStringBuilder':
        """public org.apache.commons.lang3.builder.ToStringBuilder org.apache.commons.lang3.builder.ToStringBuilder.append(java.lang.String,short)"""
        return 'ToStringBuilder'._wrap(super(_ToStringBuilder, self).append(arg0, _short.valueOf(arg1)))

    @overload
    def getObject(self) -> object:
        """public java.lang.Object org.apache.commons.lang3.builder.ToStringBuilder.getObject()"""
        return object._wrap(super(ToStringBuilder, self).getObject()) 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffResult
from builtins import str
import org.apache.commons.lang3.builder.DiffResult as _DiffResult
_DiffResult = _DiffResult
import org.apache.commons.lang3.builder.ToStringStyle as _ToStringStyle
_ToStringStyle = _ToStringStyle
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
import java.lang.String as _String
_String = _String
from builtins import object
import java.util.List as _List
_List = _List
import java.util.Iterator as Iterator
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class DiffResult():
    """org.apache.commons.lang3.builder.DiffResult"""
 
    @staticmethod
    def _wrap(java_value: _DiffResult) -> 'DiffResult':
        return DiffResult(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DiffResult):
        """
        Dynamic initializer for DiffResult.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DiffResult__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DiffResult__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDiffs(self) -> 'List':
        """public java.util.List<org.apache.commons.lang3.builder.Diff<?>> org.apache.commons.lang3.builder.DiffResult.getDiffs()"""
        return 'List'._wrap(super(DiffResult, self).getDiffs())

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

    @overload
    def getRight(self) -> object:
        """public T org.apache.commons.lang3.builder.DiffResult.getRight()"""
        return object._wrap(super(DiffResult, self).getRight())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.DiffResult.toString()"""
        return str._wrap(super(DiffResult, self).toString())

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<T> java.lang.Iterable.spliterator()"""
        return 'Spliterator'._wrap(super(Iterable, self).spliterator())

    @overload
    def getLeft(self) -> object:
        """public T org.apache.commons.lang3.builder.DiffResult.getLeft()"""
        return object._wrap(super(DiffResult, self).getLeft())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getNumberOfDiffs(self) -> int:
        """public int org.apache.commons.lang3.builder.DiffResult.getNumberOfDiffs()"""
        return int._wrap(super(DiffResult, self).getNumberOfDiffs())

    @overload
    def getToStringStyle(self) -> 'ToStringStyle':
        """public org.apache.commons.lang3.builder.ToStringStyle org.apache.commons.lang3.builder.DiffResult.getToStringStyle()"""
        return 'ToStringStyle'._wrap(super(DiffResult, self).getToStringStyle())

    @overload
    def toString(self, arg0: 'ToStringStyle') -> str:
        """public java.lang.String org.apache.commons.lang3.builder.DiffResult.toString(org.apache.commons.lang3.builder.ToStringStyle)"""
        return str._wrap(super(_DiffResult, self).toString(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<org.apache.commons.lang3.builder.Diff<?>> org.apache.commons.lang3.builder.DiffResult.iterator()"""
        return 'Iterator'._wrap(super(DiffResult, self).iterator())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.builder.EqualsBuilder
import java.lang.Boolean as Boolean
from builtins import str
import java.lang.Double as _double
import java.lang.Character as _char
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.builder.EqualsBuilder as _EqualsBuilder
_EqualsBuilder = _EqualsBuilder
from builtins import float
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Boolean as _Boolean
_Boolean = _Boolean
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.util.List as List
import java.lang.Class as _Class
_Class = _Class
 
class EqualsBuilder():
    """org.apache.commons.lang3.builder.EqualsBuilder"""
 
    @staticmethod
    def _wrap(java_value: _EqualsBuilder) -> 'EqualsBuilder':
        return EqualsBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _EqualsBuilder):
        """
        Dynamic initializer for EqualsBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_EqualsBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_EqualsBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: bool) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,boolean)"""
        return bool._wrap(_EqualsBuilder.reflectionEquals(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: str, arg1: str) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(char,char)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_char.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def append(self, arg0: 'char', arg1: 'char') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(char[],char[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setTestTransients(self, arg0: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setTestTransients(boolean)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).setTestTransients(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(short,short)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_short.valueOf(arg0), _short.valueOf(arg1)))

    @override
    @overload
    def build(self) -> 'Boolean':
        """public java.lang.Boolean org.apache.commons.lang3.builder.EqualsBuilder.build()"""
        return 'Boolean'._wrap(super(EqualsBuilder, self).build())

    @overload
    def setBypassReflectionClasses(self, arg0: 'List') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setBypassReflectionClasses(java.util.List<java.lang.Class<?>>)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).setBypassReflectionClasses(arg0))

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(byte,byte)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_byte.valueOf(arg0), _byte.valueOf(arg1)))

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

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.EqualsBuilder()"""
        val = _EqualsBuilder()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.EqualsBuilder()"""
        val = _EqualsBuilder()
        self.__wrapper = val

    @overload
    def append(self, arg0: 'double', arg1: 'double') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(double[],double[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'long', arg1: 'long') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(long[],long[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: bool, arg1: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(boolean,boolean)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_boolean.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def append(self, arg0: 'float', arg1: 'float') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(float[],float[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, *arg2: str) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,java.lang.String...)"""
        return bool._wrap(_EqualsBuilder.reflectionEquals(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def setTestRecursive(self, arg0: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setTestRecursive(boolean)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).setTestRecursive(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(int,int)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_int.valueOf(arg0), _int.valueOf(arg1)))

    @overload
    def append(self, arg0: 'short', arg1: 'short') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(short[],short[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @overload
    def isEquals(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.EqualsBuilder.isEquals()"""
        return bool._wrap(super(EqualsBuilder, self).isEquals())

    @overload
    def append(self, arg0: 'boolean', arg1: 'boolean') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(boolean[],boolean[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'int', arg1: 'int') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(int[],int[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def append(self, arg0: int, arg1: int) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(long,long)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_long.valueOf(arg0), _long.valueOf(arg1)))

    @overload
    def append(self, arg0: float, arg1: float) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(double,double)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_double.valueOf(arg0), _double.valueOf(arg1)))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: 'Collection') -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,java.util.Collection<java.lang.String>)"""
        return bool._wrap(_EqualsBuilder.reflectionEquals(arg0, arg1, arg2))

    @overload
    def append(self, arg0: 'Object', arg1: 'Object') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(java.lang.Object[],java.lang.Object[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: bool, arg3: 'Class', arg4: bool, *arg5: str) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,boolean,java.lang.Class<?>,boolean,java.lang.String...)"""
        return bool._wrap(_EqualsBuilder.reflectionEquals(arg0, arg1, _boolean.valueOf(arg2), arg3, _boolean.valueOf(arg4), arg5))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def append(self, arg0: bytes, arg1: bytes) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(byte[],byte[])"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(bytes, bytes))

    @overload
    def append(self, arg0: object, arg1: object) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(java.lang.Object,java.lang.Object)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(arg0, arg1))

    @overload
    def setReflectUpToClass(self, arg0: 'Class') -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setReflectUpToClass(java.lang.Class<?>)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).setReflectUpToClass(arg0))

    @staticmethod
    @overload
    def reflectionEquals(arg0: object, arg1: object, arg2: bool, arg3: 'Class', *arg4: str) -> bool:
        """public static boolean org.apache.commons.lang3.builder.EqualsBuilder.reflectionEquals(java.lang.Object,java.lang.Object,boolean,java.lang.Class<?>,java.lang.String...)"""
        return bool._wrap(_EqualsBuilder.reflectionEquals(arg0, arg1, _boolean.valueOf(arg2), arg3, arg4))

    @overload
    def appendSuper(self, arg0: bool) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.appendSuper(boolean)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).appendSuper(_boolean.valueOf(arg0)))

    @overload
    def reflectionAppend(self, arg0: object, arg1: object) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.reflectionAppend(java.lang.Object,java.lang.Object)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).reflectionAppend(arg0, arg1))

    @overload
    def setExcludeFields(self, *arg0: str) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.setExcludeFields(java.lang.String...)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).setExcludeFields(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def reset(self):
        """public void org.apache.commons.lang3.builder.EqualsBuilder.reset()"""
        super(EqualsBuilder, self).reset()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: float, arg1: float) -> 'EqualsBuilder':
        """public org.apache.commons.lang3.builder.EqualsBuilder org.apache.commons.lang3.builder.EqualsBuilder.append(float,float)"""
        return 'EqualsBuilder'._wrap(super(_EqualsBuilder, self).append(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as _Map
_Map = _Map
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import org.apache.commons.lang3.builder.ToStringStyle as _ToStringStyle
_ToStringStyle = _ToStringStyle
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle as _MultilineRecursiveToStringStyle
_MultilineRecursiveToStringStyle = _MultilineRecursiveToStringStyle
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MultilineRecursiveToStringStyle():
    """org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle"""
 
    @staticmethod
    def _wrap(java_value: _MultilineRecursiveToStringStyle) -> 'MultilineRecursiveToStringStyle':
        return MultilineRecursiveToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MultilineRecursiveToStringStyle):
        """
        Dynamic initializer for MultilineRecursiveToStringStyle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MultilineRecursiveToStringStyle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MultilineRecursiveToStringStyle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendEnd(arg0, arg1)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendStart(arg0, arg1)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(_ToStringStyle, self).append(arg0, arg1, _long.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(_ToStringStyle, self).append(arg0, arg1, _short.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, _boolean.valueOf(arg2))

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
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, bytes, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def appendDetail(self, arg0: 'StringBuffer', arg1: str, arg2: object):
        """public void org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle.appendDetail(java.lang.StringBuffer,java.lang.String,java.lang.Object)"""
        super(_MultilineRecursiveToStringStyle, self).appendDetail(arg0, arg1, arg2)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(_ToStringStyle, self).append(arg0, arg1, _char.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(_ToStringStyle, self).append(arg0, arg1, _int.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(_ToStringStyle, self).append(arg0, arg1, _double.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(_ToStringStyle, self).append(arg0, arg1, _byte.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle()"""
        val = _MultilineRecursiveToStringStyle()
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendToString(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.MultilineRecursiveToStringStyle()"""
        val = _MultilineRecursiveToStringStyle()
        self.__wrapper = val

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(_ToStringStyle, self).append(arg0, arg1, _float.valueOf(arg2))

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map._wrap(_ToStringStyle.getRegistry())

    @override
    @overload
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendSuper(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.builder.RecursiveToStringStyle
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as _Map
_Map = _Map
import org.apache.commons.lang3.builder.RecursiveToStringStyle as _RecursiveToStringStyle
_RecursiveToStringStyle = _RecursiveToStringStyle
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import org.apache.commons.lang3.builder.ToStringStyle as _ToStringStyle
_ToStringStyle = _ToStringStyle
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class RecursiveToStringStyle():
    """org.apache.commons.lang3.builder.RecursiveToStringStyle"""
 
    @staticmethod
    def _wrap(java_value: _RecursiveToStringStyle) -> 'RecursiveToStringStyle':
        return RecursiveToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _RecursiveToStringStyle):
        """
        Dynamic initializer for RecursiveToStringStyle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_RecursiveToStringStyle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_RecursiveToStringStyle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendEnd(arg0, arg1)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendStart(arg0, arg1)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(_ToStringStyle, self).append(arg0, arg1, _long.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(_ToStringStyle, self).append(arg0, arg1, _short.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.RecursiveToStringStyle()"""
        val = _RecursiveToStringStyle()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, bytes, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(_ToStringStyle, self).append(arg0, arg1, _char.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(_ToStringStyle, self).append(arg0, arg1, _int.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def appendDetail(self, arg0: 'StringBuffer', arg1: str, arg2: object):
        """public void org.apache.commons.lang3.builder.RecursiveToStringStyle.appendDetail(java.lang.StringBuffer,java.lang.String,java.lang.Object)"""
        super(_RecursiveToStringStyle, self).appendDetail(arg0, arg1, arg2)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(_ToStringStyle, self).append(arg0, arg1, _double.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(_ToStringStyle, self).append(arg0, arg1, _byte.valueOf(arg2))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.RecursiveToStringStyle()"""
        val = _RecursiveToStringStyle()
        self.__wrapper = val

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendToString(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(_ToStringStyle, self).append(arg0, arg1, _float.valueOf(arg2))

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map._wrap(_ToStringStyle.getRegistry())

    @override
    @overload
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendSuper(arg0, arg1)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.builder.StandardToStringStyle
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as _Map
_Map = _Map
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
import org.apache.commons.lang3.builder.StandardToStringStyle as _StandardToStringStyle
_StandardToStringStyle = _StandardToStringStyle
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import org.apache.commons.lang3.builder.ToStringStyle as _ToStringStyle
_ToStringStyle = _ToStringStyle
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.Float as _float
import java.lang.Integer as _int
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class StandardToStringStyle():
    """org.apache.commons.lang3.builder.StandardToStringStyle"""
 
    @staticmethod
    def _wrap(java_value: _StandardToStringStyle) -> 'StandardToStringStyle':
        return StandardToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _StandardToStringStyle):
        """
        Dynamic initializer for StandardToStringStyle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_StandardToStringStyle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_StandardToStringStyle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getFieldSeparator(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getFieldSeparator()"""
        return str._wrap(super(StandardToStringStyle, self).getFieldSeparator())

    @override
    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendEnd(arg0, arg1)

    @overload
    def getContentStart(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getContentStart()"""
        return str._wrap(super(StandardToStringStyle, self).getContentStart())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(_ToStringStyle, self).append(arg0, arg1, _long.valueOf(arg2))

    @overload
    def isFieldSeparatorAtEnd(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isFieldSeparatorAtEnd()"""
        return bool._wrap(super(StandardToStringStyle, self).isFieldSeparatorAtEnd())

    @overload
    def getArraySeparator(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getArraySeparator()"""
        return str._wrap(super(StandardToStringStyle, self).getArraySeparator())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(_ToStringStyle, self).append(arg0, arg1, _short.valueOf(arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.StandardToStringStyle()"""
        val = _StandardToStringStyle()
        self.__wrapper = val

    @overload
    def setDefaultFullDetail(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setDefaultFullDetail(boolean)"""
        super(_StandardToStringStyle, self).setDefaultFullDetail(_boolean.valueOf(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def setFieldNameValueSeparator(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldNameValueSeparator(java.lang.String)"""
        super(_StandardToStringStyle, self).setFieldNameValueSeparator(arg0)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, bytes, arg3)

    @overload
    def isUseClassName(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseClassName()"""
        return bool._wrap(super(StandardToStringStyle, self).isUseClassName())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(_ToStringStyle, self).append(arg0, arg1, _char.valueOf(arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def getArrayStart(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getArrayStart()"""
        return str._wrap(super(StandardToStringStyle, self).getArrayStart())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(_ToStringStyle, self).append(arg0, arg1, _int.valueOf(arg2))

    @overload
    def getFieldNameValueSeparator(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getFieldNameValueSeparator()"""
        return str._wrap(super(StandardToStringStyle, self).getFieldNameValueSeparator())

    @overload
    def setUseShortClassName(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseShortClassName(boolean)"""
        super(_StandardToStringStyle, self).setUseShortClassName(_boolean.valueOf(arg0))

    @overload
    def setUseFieldNames(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseFieldNames(boolean)"""
        super(_StandardToStringStyle, self).setUseFieldNames(_boolean.valueOf(arg0))

    @overload
    def getArrayEnd(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getArrayEnd()"""
        return str._wrap(super(StandardToStringStyle, self).getArrayEnd())

    @overload
    def getSizeStartText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSizeStartText()"""
        return str._wrap(super(StandardToStringStyle, self).getSizeStartText())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def setArrayEnd(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArrayEnd(java.lang.String)"""
        super(_StandardToStringStyle, self).setArrayEnd(arg0)

    @overload
    def setSummaryObjectStartText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSummaryObjectStartText(java.lang.String)"""
        super(_StandardToStringStyle, self).setSummaryObjectStartText(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def setContentEnd(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setContentEnd(java.lang.String)"""
        super(_StandardToStringStyle, self).setContentEnd(arg0)

    @overload
    def setArraySeparator(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArraySeparator(java.lang.String)"""
        super(_StandardToStringStyle, self).setArraySeparator(arg0)

    @overload
    def setFieldSeparatorAtEnd(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldSeparatorAtEnd(boolean)"""
        super(_StandardToStringStyle, self).setFieldSeparatorAtEnd(_boolean.valueOf(arg0))

    @overload
    def setContentStart(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setContentStart(java.lang.String)"""
        super(_StandardToStringStyle, self).setContentStart(arg0)

    @overload
    def getContentEnd(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getContentEnd()"""
        return str._wrap(super(StandardToStringStyle, self).getContentEnd())

    @override
    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendToString(arg0, arg1)

    @overload
    def isUseShortClassName(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseShortClassName()"""
        return bool._wrap(super(StandardToStringStyle, self).isUseShortClassName())

    @overload
    def isDefaultFullDetail(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isDefaultFullDetail()"""
        return bool._wrap(super(StandardToStringStyle, self).isDefaultFullDetail())

    @overload
    def getSizeEndText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSizeEndText()"""
        return str._wrap(super(StandardToStringStyle, self).getSizeEndText())

    @overload
    def getSummaryObjectStartText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSummaryObjectStartText()"""
        return str._wrap(super(StandardToStringStyle, self).getSummaryObjectStartText())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(_ToStringStyle, self).append(arg0, arg1, _float.valueOf(arg2))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def setFieldSeparatorAtStart(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldSeparatorAtStart(boolean)"""
        super(_StandardToStringStyle, self).setFieldSeparatorAtStart(_boolean.valueOf(arg0))

    @override
    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendStart(arg0, arg1)

    @overload
    def setArrayStart(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArrayStart(java.lang.String)"""
        super(_StandardToStringStyle, self).setArrayStart(arg0)

    @overload
    def setSizeEndText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSizeEndText(java.lang.String)"""
        super(_StandardToStringStyle, self).setSizeEndText(arg0)

    @overload
    def setSizeStartText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSizeStartText(java.lang.String)"""
        super(_StandardToStringStyle, self).setSizeStartText(arg0)

    @overload
    def getSummaryObjectEndText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getSummaryObjectEndText()"""
        return str._wrap(super(StandardToStringStyle, self).getSummaryObjectEndText())

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, _boolean.valueOf(arg2))

    @overload
    def getNullText(self) -> str:
        """public java.lang.String org.apache.commons.lang3.builder.StandardToStringStyle.getNullText()"""
        return str._wrap(super(StandardToStringStyle, self).getNullText())

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.StandardToStringStyle()"""
        val = _StandardToStringStyle()
        self.__wrapper = val

    @overload
    def isUseIdentityHashCode(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseIdentityHashCode()"""
        return bool._wrap(super(StandardToStringStyle, self).isUseIdentityHashCode())

    @overload
    def setUseClassName(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseClassName(boolean)"""
        super(_StandardToStringStyle, self).setUseClassName(_boolean.valueOf(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def isUseFieldNames(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isUseFieldNames()"""
        return bool._wrap(super(StandardToStringStyle, self).isUseFieldNames())

    @overload
    def setFieldSeparator(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setFieldSeparator(java.lang.String)"""
        super(_StandardToStringStyle, self).setFieldSeparator(arg0)

    @overload
    def setArrayContentDetail(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setArrayContentDetail(boolean)"""
        super(_StandardToStringStyle, self).setArrayContentDetail(_boolean.valueOf(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(_ToStringStyle, self).append(arg0, arg1, _double.valueOf(arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(_ToStringStyle, self).append(arg0, arg1, _byte.valueOf(arg2))

    @overload
    def setNullText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setNullText(java.lang.String)"""
        super(_StandardToStringStyle, self).setNullText(arg0)

    @overload
    def setSummaryObjectEndText(self, arg0: str):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setSummaryObjectEndText(java.lang.String)"""
        super(_StandardToStringStyle, self).setSummaryObjectEndText(arg0)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def isArrayContentDetail(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isArrayContentDetail()"""
        return bool._wrap(super(StandardToStringStyle, self).isArrayContentDetail())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isFieldSeparatorAtStart(self) -> bool:
        """public boolean org.apache.commons.lang3.builder.StandardToStringStyle.isFieldSeparatorAtStart()"""
        return bool._wrap(super(StandardToStringStyle, self).isFieldSeparatorAtStart())

    @overload
    def setUseIdentityHashCode(self, arg0: bool):
        """public void org.apache.commons.lang3.builder.StandardToStringStyle.setUseIdentityHashCode(boolean)"""
        super(_StandardToStringStyle, self).setUseIdentityHashCode(_boolean.valueOf(arg0))

    @override
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map._wrap(_ToStringStyle.getRegistry())

    @override
    @overload
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendSuper(arg0, arg1) 
 
 
# CLASS: org.apache.commons.lang3.builder.CompareToBuilder
from builtins import str
import java.lang.Double as _double
import java.lang.Character as _char
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import float
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.util.Comparator as Comparator
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.lang.Integer as Integer
import org.apache.commons.lang3.builder.CompareToBuilder as _CompareToBuilder
_CompareToBuilder = _CompareToBuilder
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class CompareToBuilder():
    """org.apache.commons.lang3.builder.CompareToBuilder"""
 
    @staticmethod
    def _wrap(java_value: _CompareToBuilder) -> 'CompareToBuilder':
        return CompareToBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _CompareToBuilder):
        """
        Dynamic initializer for CompareToBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_CompareToBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_CompareToBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object)"""
        return int._wrap(_CompareToBuilder.reflectionCompare(arg0, arg1))

    @overload
    def append(self, arg0: 'int', arg1: 'int') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(int[],int[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'char', arg1: 'char') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(char[],char[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(byte,byte)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_byte.valueOf(arg0), _byte.valueOf(arg1)))

    @overload
    def append(self, arg0: 'Object', arg1: 'Object', arg2: 'Comparator') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object[],java.lang.Object[],java.util.Comparator<?>)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: str, arg1: str) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(char,char)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_char.valueOf(arg0), _char.valueOf(arg1)))

    @overload
    def toComparison(self) -> int:
        """public int org.apache.commons.lang3.builder.CompareToBuilder.toComparison()"""
        return int._wrap(super(CompareToBuilder, self).toComparison())

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, *arg2: str) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,java.lang.String...)"""
        return int._wrap(_CompareToBuilder.reflectionCompare(arg0, arg1, arg2))

    @overload
    def append(self, arg0: 'short', arg1: 'short') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(short[],short[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(int,int)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_int.valueOf(arg0), _int.valueOf(arg1)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(long,long)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_long.valueOf(arg0), _long.valueOf(arg1)))

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, arg2: bool, arg3: 'Class', *arg4: str) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,boolean,java.lang.Class<?>,java.lang.String...)"""
        return int._wrap(_CompareToBuilder.reflectionCompare(arg0, arg1, _boolean.valueOf(arg2), arg3, arg4))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.CompareToBuilder()"""
        val = _CompareToBuilder()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.CompareToBuilder()"""
        val = _CompareToBuilder()
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def append(self, arg0: object, arg1: object, arg2: 'Comparator') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object,java.lang.Object,java.util.Comparator<?>)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1, arg2))

    @override
    @overload
    def build(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.builder.CompareToBuilder.build()"""
        return _transform(super(CompareToBuilder, self).build()).'Integer'Value()

    @overload
    def appendSuper(self, arg0: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.appendSuper(int)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).appendSuper(_int.valueOf(arg0)))

    @overload
    def append(self, arg0: 'Object', arg1: 'Object') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object[],java.lang.Object[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: int, arg1: int) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(short,short)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_short.valueOf(arg0), _short.valueOf(arg1)))

    @overload
    def append(self, arg0: float, arg1: float) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(float,float)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_float.valueOf(arg0), _float.valueOf(arg1)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, arg2: 'Collection') -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,java.util.Collection<java.lang.String>)"""
        return int._wrap(_CompareToBuilder.reflectionCompare(arg0, arg1, arg2))

    @staticmethod
    @overload
    def reflectionCompare(arg0: object, arg1: object, arg2: bool) -> int:
        """public static int org.apache.commons.lang3.builder.CompareToBuilder.reflectionCompare(java.lang.Object,java.lang.Object,boolean)"""
        return int._wrap(_CompareToBuilder.reflectionCompare(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def append(self, arg0: 'long', arg1: 'long') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(long[],long[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: 'boolean', arg1: 'boolean') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(boolean[],boolean[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def append(self, arg0: object, arg1: object) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(java.lang.Object,java.lang.Object)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: 'float', arg1: 'float') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(float[],float[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @overload
    def append(self, arg0: bool, arg1: bool) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(boolean,boolean)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_boolean.valueOf(arg0), _boolean.valueOf(arg1)))

    @overload
    def append(self, arg0: float, arg1: float) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(double,double)"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(_double.valueOf(arg0), _double.valueOf(arg1)))

    @overload
    def append(self, arg0: bytes, arg1: bytes) -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(byte[],byte[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(bytes, bytes))

    @overload
    def append(self, arg0: 'double', arg1: 'double') -> 'CompareToBuilder':
        """public org.apache.commons.lang3.builder.CompareToBuilder org.apache.commons.lang3.builder.CompareToBuilder.append(double[],double[])"""
        return 'CompareToBuilder'._wrap(super(_CompareToBuilder, self).append(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.builder.ReflectionDiffBuilder
from builtins import str
import org.apache.commons.lang3.builder.DiffResult as _DiffResult
_DiffResult = _DiffResult
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.builder.ReflectionDiffBuilder as _ReflectionDiffBuilder
_ReflectionDiffBuilder = _ReflectionDiffBuilder
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReflectionDiffBuilder():
    """org.apache.commons.lang3.builder.ReflectionDiffBuilder"""
 
    @staticmethod
    def _wrap(java_value: _ReflectionDiffBuilder) -> 'ReflectionDiffBuilder':
        return ReflectionDiffBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectionDiffBuilder):
        """
        Dynamic initializer for ReflectionDiffBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectionDiffBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectionDiffBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: object, arg1: object, arg2: 'ToStringStyle'):
        """public org.apache.commons.lang3.builder.ReflectionDiffBuilder(T,T,org.apache.commons.lang3.builder.ToStringStyle)"""
        val = _ReflectionDiffBuilder(arg0, arg1, arg2)
        self.__wrapper = val

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
    def setExcludeFieldNames(self, *arg0: str) -> 'ReflectionDiffBuilder':
        """public org.apache.commons.lang3.builder.ReflectionDiffBuilder<T> org.apache.commons.lang3.builder.ReflectionDiffBuilder.setExcludeFieldNames(java.lang.String...)"""
        return 'ReflectionDiffBuilder'._wrap(super(_ReflectionDiffBuilder, self).setExcludeFieldNames(arg0))

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

    @overload
    def getExcludeFieldNames(self) -> List[str]:
        """public java.lang.String[] org.apache.commons.lang3.builder.ReflectionDiffBuilder.getExcludeFieldNames()"""
        return List[str]._wrap(super(ReflectionDiffBuilder, self).getExcludeFieldNames())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def build(self) -> 'DiffResult':
        """public org.apache.commons.lang3.builder.DiffResult<T> org.apache.commons.lang3.builder.ReflectionDiffBuilder.build()"""
        return 'DiffResult'._wrap(super(ReflectionDiffBuilder, self).build())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.builder.Diffable
from abc import abstractmethod, ABC
import org.apache.commons.lang3.builder.Diffable as _Diffable
_Diffable = _Diffable
 
class Diffable():
    """org.apache.commons.lang3.builder.Diffable"""
 
    @staticmethod
    def _wrap(java_value: _Diffable) -> 'Diffable':
        return Diffable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Diffable):
        """
        Dynamic initializer for Diffable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Diffable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Diffable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def diff(self, arg0: object):
        """public abstract org.apache.commons.lang3.builder.DiffResult<T> org.apache.commons.lang3.builder.Diffable.diff(T)"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.builder.DiffExclude
import org.apache.commons.lang3.builder.DiffExclude as _DiffExclude
_DiffExclude = _DiffExclude
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
 
class DiffExclude():
    """org.apache.commons.lang3.builder.DiffExclude"""
 
    @staticmethod
    def _wrap(java_value: _DiffExclude) -> 'DiffExclude':
        return DiffExclude(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _DiffExclude):
        """
        Dynamic initializer for DiffExclude.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_DiffExclude__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_DiffExclude__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
 
 
# CLASS: org.apache.commons.lang3.builder.ToStringStyle
import java.lang.Character as _char
import java.lang.Double as _double
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.StringBuffer as StringBuffer
import java.util.Map as _Map
_Map = _Map
import java.lang.Short as _short
import java.lang.String as _string
import java.lang.Boolean as _boolean
import java.lang.Byte as _byte
from builtins import bool
import java.lang.Boolean as Boolean
from builtins import str
import org.apache.commons.lang3.builder.ToStringStyle as _ToStringStyle
_ToStringStyle = _ToStringStyle
from pyquantum_helper import override
import java.lang.Object as _object
from builtins import float
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Float as _float
import java.lang.Integer as _int
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ToStringStyle():
    """org.apache.commons.lang3.builder.ToStringStyle"""
 
    @staticmethod
    def _wrap(java_value: _ToStringStyle) -> 'ToStringStyle':
        return ToStringStyle(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ToStringStyle):
        """
        Dynamic initializer for ToStringStyle.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ToStringStyle__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ToStringStyle__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bool):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, _boolean.valueOf(arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'short', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'double', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def appendToString(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendToString(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendToString(arg0, arg1)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long)"""
        super(_ToStringStyle, self).append(arg0, arg1, _long.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'char', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,double)"""
        super(_ToStringStyle, self).append(arg0, arg1, _double.valueOf(arg2))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'int', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'Object', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def appendStart(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendStart(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendStart(arg0, arg1)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,short)"""
        super(_ToStringStyle, self).append(arg0, arg1, _short.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: bytes, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, bytes, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'boolean', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,boolean[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,int)"""
        super(_ToStringStyle, self).append(arg0, arg1, _int.valueOf(arg2))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: object, arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,java.lang.Object,java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,char)"""
        super(_ToStringStyle, self).append(arg0, arg1, _char.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'float', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: float):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,float)"""
        super(_ToStringStyle, self).append(arg0, arg1, _float.valueOf(arg2))

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: 'long', arg3: 'Boolean'):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,long[],java.lang.Boolean)"""
        super(_ToStringStyle, self).append(arg0, arg1, arg2, arg3)

    @overload
    def appendEnd(self, arg0: 'StringBuffer', arg1: object):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendEnd(java.lang.StringBuffer,java.lang.Object)"""
        super(_ToStringStyle, self).appendEnd(arg0, arg1)

    @overload
    def append(self, arg0: 'StringBuffer', arg1: str, arg2: int):
        """public void org.apache.commons.lang3.builder.ToStringStyle.append(java.lang.StringBuffer,java.lang.String,byte)"""
        super(_ToStringStyle, self).append(arg0, arg1, _byte.valueOf(arg2))

    @overload
    def appendSuper(self, arg0: 'StringBuffer', arg1: str):
        """public void org.apache.commons.lang3.builder.ToStringStyle.appendSuper(java.lang.StringBuffer,java.lang.String)"""
        super(_ToStringStyle, self).appendSuper(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getRegistry() -> 'Map':
        """public static java.util.Map<java.lang.Object, java.lang.Object> org.apache.commons.lang3.builder.ToStringStyle.getRegistry()"""
        return Map._wrap(_ToStringStyle.getRegistry())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.builder.HashCodeBuilder
from builtins import str
import java.lang.Character as _char
import java.lang.Double as _double
from pyquantum_helper import transform as _transform
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.builder.HashCodeBuilder as _HashCodeBuilder
_HashCodeBuilder = _HashCodeBuilder
from builtins import float
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Short as _short
import java.lang.Float as _float
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.Byte as _byte
import java.lang.Integer as Integer
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class HashCodeBuilder():
    """org.apache.commons.lang3.builder.HashCodeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _HashCodeBuilder) -> 'HashCodeBuilder':
        return HashCodeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _HashCodeBuilder):
        """
        Dynamic initializer for HashCodeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_HashCodeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_HashCodeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def append(self, arg0: 'float') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(float[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @overload
    def appendSuper(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.appendSuper(int)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).appendSuper(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: object, arg1: bool) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(java.lang.Object,boolean)"""
        return int._wrap(_HashCodeBuilder.reflectionHashCode(arg0, _boolean.valueOf(arg1)))

    @overload
    def append(self, arg0: 'short') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(short[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'long') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(long[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: bool) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(boolean)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_boolean.valueOf(arg0)))

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(byte)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_byte.valueOf(arg0)))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def append(self, arg0: 'char') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(char[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @override
    @overload
    def build(self) -> 'Integer':
        """public java.lang.Integer org.apache.commons.lang3.builder.HashCodeBuilder.build()"""
        return _transform(super(HashCodeBuilder, self).build()).'Integer'Value()

    @overload
    def append(self, arg0: 'Object') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(java.lang.Object[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.builder.HashCodeBuilder.hashCode()"""
        return int._wrap(super(HashCodeBuilder, self).hashCode())

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

    @overload
    def append(self, arg0: bytes) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(byte[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(bytes))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: int, arg1: int, arg2: object, arg3: bool, arg4: 'Class', *arg5: str) -> int:
        """public static <T> int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(int,int,T,boolean,java.lang.Class<? super T>,java.lang.String...)"""
        return int._wrap(_HashCodeBuilder.reflectionHashCode(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _boolean.valueOf(arg3), arg4, arg5))

    @overload
    def append(self, arg0: str) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(char)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_char.valueOf(arg0)))

    @overload
    def __init__(self, arg0: int, arg1: int):
        """public org.apache.commons.lang3.builder.HashCodeBuilder(int,int)"""
        val = _HashCodeBuilder(_int.valueOf(arg0), _int.valueOf(arg1))
        self.__wrapper = val

    @overload
    def append(self, arg0: object) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(java.lang.Object)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(short)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_short.valueOf(arg0)))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean org.apache.commons.lang3.builder.HashCodeBuilder.equals(java.lang.Object)"""
        return bool._wrap(super(_HashCodeBuilder, self).equals(arg0))

    @overload
    def toHashCode(self) -> int:
        """public int org.apache.commons.lang3.builder.HashCodeBuilder.toHashCode()"""
        return int._wrap(super(HashCodeBuilder, self).toHashCode())

    @staticmethod
    @overload
    def reflectionHashCode(arg0: object, arg1: 'Collection') -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(java.lang.Object,java.util.Collection<java.lang.String>)"""
        return int._wrap(_HashCodeBuilder.reflectionHashCode(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: object, *arg1: str) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(java.lang.Object,java.lang.String...)"""
        return int._wrap(_HashCodeBuilder.reflectionHashCode(arg0, arg1))

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(int)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_int.valueOf(arg0)))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: int, arg1: int, arg2: object, arg3: bool) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(int,int,java.lang.Object,boolean)"""
        return int._wrap(_HashCodeBuilder.reflectionHashCode(_int.valueOf(arg0), _int.valueOf(arg1), arg2, _boolean.valueOf(arg3)))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def append(self, arg0: 'double') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(double[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @overload
    def append(self, arg0: 'boolean') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(boolean[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.builder.HashCodeBuilder()"""
        val = _HashCodeBuilder()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def append(self, arg0: float) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(float)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_float.valueOf(arg0)))

    @staticmethod
    @overload
    def reflectionHashCode(arg0: int, arg1: int, arg2: object) -> int:
        """public static int org.apache.commons.lang3.builder.HashCodeBuilder.reflectionHashCode(int,int,java.lang.Object)"""
        return int._wrap(_HashCodeBuilder.reflectionHashCode(_int.valueOf(arg0), _int.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.builder.HashCodeBuilder()"""
        val = _HashCodeBuilder()
        self.__wrapper = val

    @overload
    def append(self, arg0: int) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(long)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_long.valueOf(arg0)))

    @overload
    def append(self, arg0: float) -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(double)"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(_double.valueOf(arg0)))

    @overload
    def append(self, arg0: 'int') -> 'HashCodeBuilder':
        """public org.apache.commons.lang3.builder.HashCodeBuilder org.apache.commons.lang3.builder.HashCodeBuilder.append(int[])"""
        return 'HashCodeBuilder'._wrap(super(_HashCodeBuilder, self).append(arg0))