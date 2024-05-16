from __future__ import annotations
from overload import overload


 
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Field as Field
import java.lang.reflect.Constructor as __Constructor
__Constructor = __Constructor
import java.lang.IllegalAccessException as IllegalAccessException
from typing import List
import com.google.gson.internal.reflect.ReflectionHelper as __ReflectionHelper
__ReflectionHelper = __ReflectionHelper
import java.lang.RuntimeException as __RuntimeException
__RuntimeException = __RuntimeException
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.reflect.Method as __Method
__Method = __Method
import java.lang.RuntimeException as RuntimeException
import java.lang.reflect.AccessibleObject as AccessibleObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.Method as Method
import java.lang.reflect.Constructor as Constructor
from builtins import int
 
class ReflectionHelper():
    """com.google.gson.internal.reflect.ReflectionHelper"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionHelper) -> 'ReflectionHelper':
        return ReflectionHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionHelper):
        """
        Dynamic initializer for ReflectionHelper.
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
 
    @staticmethod
    @overload
    def getCanonicalRecordConstructor(arg0: 'Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> com.google.gson.internal.reflect.ReflectionHelper.getCanonicalRecordConstructor(java.lang.Class<T>)"""
        return Constructor.__wrap(__ReflectionHelper.getCanonicalRecordConstructor(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getAccessibleObjectDescription(arg0: 'AccessibleObject', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.getAccessibleObjectDescription(java.lang.reflect.AccessibleObject,boolean)"""
        return str.__wrap(__ReflectionHelper.getAccessibleObjectDescription(arg0, __boolean.valueOf(arg1)))

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

    @staticmethod
    @overload
    def getRecordComponentNames(arg0: 'Class') -> List[str]:
        """public static java.lang.String[] com.google.gson.internal.reflect.ReflectionHelper.getRecordComponentNames(java.lang.Class<?>)"""
        return List[str].__wrap(__ReflectionHelper.getRecordComponentNames(arg0))

    @staticmethod
    @overload
    def makeAccessible(arg0: 'AccessibleObject'):
        """public static void com.google.gson.internal.reflect.ReflectionHelper.makeAccessible(java.lang.reflect.AccessibleObject) throws com.google.gson.JsonIOException"""
        __ReflectionHelper.makeAccessible(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def fieldToString(arg0: 'Field') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.fieldToString(java.lang.reflect.Field)"""
        return str.__wrap(__ReflectionHelper.fieldToString(arg0))

    @staticmethod
    @overload
    def isRecord(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.reflect.ReflectionHelper.isRecord(java.lang.Class<?>)"""
        return bool.__wrap(__ReflectionHelper.isRecord(arg0))

    @staticmethod
    @overload
    def createExceptionForUnexpectedIllegalAccess(arg0: 'IllegalAccessException') -> 'RuntimeException':
        """public static java.lang.RuntimeException com.google.gson.internal.reflect.ReflectionHelper.createExceptionForUnexpectedIllegalAccess(java.lang.IllegalAccessException)"""
        return RuntimeException.__wrap(__ReflectionHelper.createExceptionForUnexpectedIllegalAccess(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getAccessor(arg0: 'Class', arg1: 'Field') -> 'Method':
        """public static java.lang.reflect.Method com.google.gson.internal.reflect.ReflectionHelper.getAccessor(java.lang.Class<?>,java.lang.reflect.Field)"""
        return Method.__wrap(__ReflectionHelper.getAccessor(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def tryMakeAccessible(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.tryMakeAccessible(java.lang.reflect.Constructor<?>)"""
        return str.__wrap(__ReflectionHelper.tryMakeAccessible(arg0))

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

    @staticmethod
    @overload
    def constructorToString(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.constructorToString(java.lang.reflect.Constructor<?>)"""
        return str.__wrap(__ReflectionHelper.constructorToString(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.gson.internal.reflect.ReflectionHelper
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Field as Field
import java.lang.reflect.Constructor as __Constructor
__Constructor = __Constructor
import java.lang.IllegalAccessException as IllegalAccessException
from typing import List
import com.google.gson.internal.reflect.ReflectionHelper as __ReflectionHelper
__ReflectionHelper = __ReflectionHelper
import java.lang.RuntimeException as __RuntimeException
__RuntimeException = __RuntimeException
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.reflect.Method as __Method
__Method = __Method
import java.lang.RuntimeException as RuntimeException
import java.lang.reflect.AccessibleObject as AccessibleObject
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.Method as Method
import java.lang.reflect.Constructor as Constructor
from builtins import int
 
class ReflectionHelper():
    """com.google.gson.internal.reflect.ReflectionHelper"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionHelper) -> 'ReflectionHelper':
        return ReflectionHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionHelper):
        """
        Dynamic initializer for ReflectionHelper.
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
 
    @staticmethod
    @overload
    def getCanonicalRecordConstructor(arg0: 'Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> com.google.gson.internal.reflect.ReflectionHelper.getCanonicalRecordConstructor(java.lang.Class<T>)"""
        return Constructor.__wrap(__ReflectionHelper.getCanonicalRecordConstructor(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getAccessibleObjectDescription(arg0: 'AccessibleObject', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.getAccessibleObjectDescription(java.lang.reflect.AccessibleObject,boolean)"""
        return str.__wrap(__ReflectionHelper.getAccessibleObjectDescription(arg0, __boolean.valueOf(arg1)))

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

    @staticmethod
    @overload
    def getRecordComponentNames(arg0: 'Class') -> List[str]:
        """public static java.lang.String[] com.google.gson.internal.reflect.ReflectionHelper.getRecordComponentNames(java.lang.Class<?>)"""
        return List[str].__wrap(__ReflectionHelper.getRecordComponentNames(arg0))

    @staticmethod
    @overload
    def makeAccessible(arg0: 'AccessibleObject'):
        """public static void com.google.gson.internal.reflect.ReflectionHelper.makeAccessible(java.lang.reflect.AccessibleObject) throws com.google.gson.JsonIOException"""
        __ReflectionHelper.makeAccessible(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def fieldToString(arg0: 'Field') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.fieldToString(java.lang.reflect.Field)"""
        return str.__wrap(__ReflectionHelper.fieldToString(arg0))

    @staticmethod
    @overload
    def isRecord(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.reflect.ReflectionHelper.isRecord(java.lang.Class<?>)"""
        return bool.__wrap(__ReflectionHelper.isRecord(arg0))

    @staticmethod
    @overload
    def createExceptionForUnexpectedIllegalAccess(arg0: 'IllegalAccessException') -> 'RuntimeException':
        """public static java.lang.RuntimeException com.google.gson.internal.reflect.ReflectionHelper.createExceptionForUnexpectedIllegalAccess(java.lang.IllegalAccessException)"""
        return RuntimeException.__wrap(__ReflectionHelper.createExceptionForUnexpectedIllegalAccess(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getAccessor(arg0: 'Class', arg1: 'Field') -> 'Method':
        """public static java.lang.reflect.Method com.google.gson.internal.reflect.ReflectionHelper.getAccessor(java.lang.Class<?>,java.lang.reflect.Field)"""
        return Method.__wrap(__ReflectionHelper.getAccessor(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def tryMakeAccessible(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.tryMakeAccessible(java.lang.reflect.Constructor<?>)"""
        return str.__wrap(__ReflectionHelper.tryMakeAccessible(arg0))

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

    @staticmethod
    @overload
    def constructorToString(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.constructorToString(java.lang.reflect.Constructor<?>)"""
        return str.__wrap(__ReflectionHelper.constructorToString(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

 
 
 
# CLASS: com.google.gson.internal.reflect.ReflectionHelper