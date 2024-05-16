from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.reflect.Type as _Type
_Type = _Type
import java.lang.Integer as _int
import com.google.gson.reflect.TypeToken as _TypeToken
_TypeToken = _TypeToken
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TypeToken():
    """com.google.gson.reflect.TypeToken"""
 
    @staticmethod
    def _wrap(java_value: _TypeToken) -> 'TypeToken':
        return TypeToken(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeToken):
        """
        Dynamic initializer for TypeToken.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeToken__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeToken__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isAssignableFrom(self, arg0: 'TypeToken') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(com.google.gson.reflect.TypeToken<?>)"""
        return bool._wrap(super(_TypeToken, self).isAssignableFrom(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Class') -> 'TypeToken':
        """public static <T> com.google.gson.reflect.TypeToken<T> com.google.gson.reflect.TypeToken.get(java.lang.Class<T>)"""
        return TypeToken._wrap(_TypeToken.get(arg0))

    @overload
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type com.google.gson.reflect.TypeToken.getType()"""
        return 'Type'._wrap(super(TypeToken, self).getType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isAssignableFrom(self, arg0: 'Type') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.reflect.Type)"""
        return bool._wrap(super(_TypeToken, self).isAssignableFrom(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean com.google.gson.reflect.TypeToken.equals(java.lang.Object)"""
        return bool._wrap(super(_TypeToken, self).equals(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.get(java.lang.reflect.Type)"""
        return TypeToken._wrap(_TypeToken.get(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.gson.reflect.TypeToken.hashCode()"""
        return int._wrap(super(TypeToken, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String com.google.gson.reflect.TypeToken.toString()"""
        return str._wrap(super(TypeToken, self).toString())

    @overload
    def isAssignableFrom(self, arg0: 'Class') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.Class<?>)"""
        return bool._wrap(super(_TypeToken, self).isAssignableFrom(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getArray(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getArray(java.lang.reflect.Type)"""
        return TypeToken._wrap(_TypeToken.getArray(arg0))

    @staticmethod
    @overload
    def getParameterized(arg0: 'Type', *arg1: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getParameterized(java.lang.reflect.Type,java.lang.reflect.Type...)"""
        return TypeToken._wrap(_TypeToken.getParameterized(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRawType(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.gson.reflect.TypeToken.getRawType()"""
        return 'type.Class'._wrap(super(TypeToken, self).getRawType())

 
 
 
# CLASS: com.google.gson.reflect.TypeToken
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.reflect.Type as _Type
_Type = _Type
import java.lang.Integer as _int
import com.google.gson.reflect.TypeToken as _TypeToken
_TypeToken = _TypeToken
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TypeToken():
    """com.google.gson.reflect.TypeToken"""
 
    @staticmethod
    def _wrap(java_value: _TypeToken) -> 'TypeToken':
        return TypeToken(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeToken):
        """
        Dynamic initializer for TypeToken.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeToken__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeToken__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isAssignableFrom(self, arg0: 'TypeToken') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(com.google.gson.reflect.TypeToken<?>)"""
        return bool._wrap(super(_TypeToken, self).isAssignableFrom(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Class') -> 'TypeToken':
        """public static <T> com.google.gson.reflect.TypeToken<T> com.google.gson.reflect.TypeToken.get(java.lang.Class<T>)"""
        return TypeToken._wrap(_TypeToken.get(arg0))

    @overload
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type com.google.gson.reflect.TypeToken.getType()"""
        return 'Type'._wrap(super(TypeToken, self).getType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isAssignableFrom(self, arg0: 'Type') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.reflect.Type)"""
        return bool._wrap(super(_TypeToken, self).isAssignableFrom(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean com.google.gson.reflect.TypeToken.equals(java.lang.Object)"""
        return bool._wrap(super(_TypeToken, self).equals(arg0))

    @staticmethod
    @overload
    def get(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.get(java.lang.reflect.Type)"""
        return TypeToken._wrap(_TypeToken.get(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.gson.reflect.TypeToken.hashCode()"""
        return int._wrap(super(TypeToken, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String com.google.gson.reflect.TypeToken.toString()"""
        return str._wrap(super(TypeToken, self).toString())

    @overload
    def isAssignableFrom(self, arg0: 'Class') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.Class<?>)"""
        return bool._wrap(super(_TypeToken, self).isAssignableFrom(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getArray(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getArray(java.lang.reflect.Type)"""
        return TypeToken._wrap(_TypeToken.getArray(arg0))

    @staticmethod
    @overload
    def getParameterized(arg0: 'Type', *arg1: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getParameterized(java.lang.reflect.Type,java.lang.reflect.Type...)"""
        return TypeToken._wrap(_TypeToken.getParameterized(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getRawType(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.gson.reflect.TypeToken.getRawType()"""
        return 'type.Class'._wrap(super(TypeToken, self).getRawType())

 
 
 
# CLASS: com.google.gson.reflect.TypeToken