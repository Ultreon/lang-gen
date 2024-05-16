from __future__ import annotations
from overload import overload


 
import com.google.gson.reflect.TypeToken as __TypeToken
__TypeToken = __TypeToken
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TypeToken():
    """com.google.gson.reflect.TypeToken"""
 
    @staticmethod
    def __wrap(java_value: __TypeToken) -> 'TypeToken':
        return TypeToken(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeToken):
        """
        Dynamic initializer for TypeToken.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isAssignableFrom(self, arg0: 'Type') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.reflect.Type)"""
        return bool.__wrap(super(__TypeToken, self).isAssignableFrom(arg0))

    @overload
    def isAssignableFrom(self, arg0: 'TypeToken') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(com.google.gson.reflect.TypeToken<?>)"""
        return bool.__wrap(super(__TypeToken, self).isAssignableFrom(arg0))

    @overload
    def getRawType(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.gson.reflect.TypeToken.getRawType()"""
        return 'type.Class'.__wrap(super(TypeToken, self).getRawType())

    @overload
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type com.google.gson.reflect.TypeToken.getType()"""
        return 'Type'.__wrap(super(TypeToken, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def get(arg0: 'Class') -> 'TypeToken':
        """public static <T> com.google.gson.reflect.TypeToken<T> com.google.gson.reflect.TypeToken.get(java.lang.Class<T>)"""
        return TypeToken.__wrap(__TypeToken.get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String com.google.gson.reflect.TypeToken.toString()"""
        return str.__wrap(super(TypeToken, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean com.google.gson.reflect.TypeToken.equals(java.lang.Object)"""
        return bool.__wrap(super(__TypeToken, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getParameterized(arg0: 'Type', *arg1: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getParameterized(java.lang.reflect.Type,java.lang.reflect.Type...)"""
        return TypeToken.__wrap(__TypeToken.getParameterized(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.get(java.lang.reflect.Type)"""
        return TypeToken.__wrap(__TypeToken.get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.gson.reflect.TypeToken.hashCode()"""
        return int.__wrap(super(TypeToken, self).hashCode())

    @staticmethod
    @overload
    def getArray(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getArray(java.lang.reflect.Type)"""
        return TypeToken.__wrap(__TypeToken.getArray(arg0))

    @overload
    def isAssignableFrom(self, arg0: 'Class') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.Class<?>)"""
        return bool.__wrap(super(__TypeToken, self).isAssignableFrom(arg0))

 
 
 
# CLASS: com.google.gson.reflect.TypeToken
import com.google.gson.reflect.TypeToken as __TypeToken
__TypeToken = __TypeToken
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class TypeToken():
    """com.google.gson.reflect.TypeToken"""
 
    @staticmethod
    def __wrap(java_value: __TypeToken) -> 'TypeToken':
        return TypeToken(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeToken):
        """
        Dynamic initializer for TypeToken.
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
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isAssignableFrom(self, arg0: 'Type') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.reflect.Type)"""
        return bool.__wrap(super(__TypeToken, self).isAssignableFrom(arg0))

    @overload
    def isAssignableFrom(self, arg0: 'TypeToken') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(com.google.gson.reflect.TypeToken<?>)"""
        return bool.__wrap(super(__TypeToken, self).isAssignableFrom(arg0))

    @overload
    def getRawType(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.gson.reflect.TypeToken.getRawType()"""
        return 'type.Class'.__wrap(super(TypeToken, self).getRawType())

    @overload
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type com.google.gson.reflect.TypeToken.getType()"""
        return 'Type'.__wrap(super(TypeToken, self).getType())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def get(arg0: 'Class') -> 'TypeToken':
        """public static <T> com.google.gson.reflect.TypeToken<T> com.google.gson.reflect.TypeToken.get(java.lang.Class<T>)"""
        return TypeToken.__wrap(__TypeToken.get(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public final java.lang.String com.google.gson.reflect.TypeToken.toString()"""
        return str.__wrap(super(TypeToken, self).toString())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean com.google.gson.reflect.TypeToken.equals(java.lang.Object)"""
        return bool.__wrap(super(__TypeToken, self).equals(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getParameterized(arg0: 'Type', *arg1: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getParameterized(java.lang.reflect.Type,java.lang.reflect.Type...)"""
        return TypeToken.__wrap(__TypeToken.getParameterized(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def get(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.get(java.lang.reflect.Type)"""
        return TypeToken.__wrap(__TypeToken.get(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public final int com.google.gson.reflect.TypeToken.hashCode()"""
        return int.__wrap(super(TypeToken, self).hashCode())

    @staticmethod
    @overload
    def getArray(arg0: 'Type') -> 'TypeToken':
        """public static com.google.gson.reflect.TypeToken<?> com.google.gson.reflect.TypeToken.getArray(java.lang.reflect.Type)"""
        return TypeToken.__wrap(__TypeToken.getArray(arg0))

    @overload
    def isAssignableFrom(self, arg0: 'Class') -> bool:
        """public boolean com.google.gson.reflect.TypeToken.isAssignableFrom(java.lang.Class<?>)"""
        return bool.__wrap(super(__TypeToken, self).isAssignableFrom(arg0))

 
 
 
# CLASS: com.google.gson.reflect.TypeToken