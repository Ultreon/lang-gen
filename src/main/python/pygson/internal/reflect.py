from __future__ import annotations
from overload import overload


 
from builtins import str
import com.google.gson.internal.reflect.ReflectionHelper as _ReflectionHelper
_ReflectionHelper = _ReflectionHelper
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.Field as Field
import java.lang.reflect.Method as _Method
_Method = _Method
import java.lang.String as _String
_String = _String
import java.lang.IllegalAccessException as IllegalAccessException
from typing import List
import java.lang.reflect.Constructor as _Constructor
_Constructor = _Constructor
import java.lang.RuntimeException as _RuntimeException
_RuntimeException = _RuntimeException
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.RuntimeException as RuntimeException
import java.lang.reflect.AccessibleObject as AccessibleObject
from builtins import bool
import java.lang.Long as _long
import java.lang.reflect.Method as Method
import java.lang.reflect.Constructor as Constructor
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReflectionHelper():
    """com.google.gson.internal.reflect.ReflectionHelper"""
 
    @staticmethod
    def _wrap(java_value: _ReflectionHelper) -> 'ReflectionHelper':
        return ReflectionHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectionHelper):
        """
        Dynamic initializer for ReflectionHelper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectionHelper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectionHelper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def tryMakeAccessible(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.tryMakeAccessible(java.lang.reflect.Constructor<?>)"""
        return str._wrap(_ReflectionHelper.tryMakeAccessible(arg0))

    @staticmethod
    @overload
    def getRecordComponentNames(arg0: 'Class') -> List[str]:
        """public static java.lang.String[] com.google.gson.internal.reflect.ReflectionHelper.getRecordComponentNames(java.lang.Class<?>)"""
        return List[str]._wrap(_ReflectionHelper.getRecordComponentNames(arg0))

    @staticmethod
    @overload
    def fieldToString(arg0: 'Field') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.fieldToString(java.lang.reflect.Field)"""
        return str._wrap(_ReflectionHelper.fieldToString(arg0))

    @staticmethod
    @overload
    def constructorToString(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.constructorToString(java.lang.reflect.Constructor<?>)"""
        return str._wrap(_ReflectionHelper.constructorToString(arg0))

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

    @staticmethod
    @overload
    def getAccessibleObjectDescription(arg0: 'AccessibleObject', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.getAccessibleObjectDescription(java.lang.reflect.AccessibleObject,boolean)"""
        return str._wrap(_ReflectionHelper.getAccessibleObjectDescription(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def makeAccessible(arg0: 'AccessibleObject'):
        """public static void com.google.gson.internal.reflect.ReflectionHelper.makeAccessible(java.lang.reflect.AccessibleObject) throws com.google.gson.JsonIOException"""
        _ReflectionHelper.makeAccessible(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getCanonicalRecordConstructor(arg0: 'Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> com.google.gson.internal.reflect.ReflectionHelper.getCanonicalRecordConstructor(java.lang.Class<T>)"""
        return Constructor._wrap(_ReflectionHelper.getCanonicalRecordConstructor(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getAccessor(arg0: 'Class', arg1: 'Field') -> 'Method':
        """public static java.lang.reflect.Method com.google.gson.internal.reflect.ReflectionHelper.getAccessor(java.lang.Class<?>,java.lang.reflect.Field)"""
        return Method._wrap(_ReflectionHelper.getAccessor(arg0, arg1))

    @staticmethod
    @overload
    def isRecord(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.reflect.ReflectionHelper.isRecord(java.lang.Class<?>)"""
        return bool._wrap(_ReflectionHelper.isRecord(arg0))

    @staticmethod
    @overload
    def createExceptionForUnexpectedIllegalAccess(arg0: 'IllegalAccessException') -> 'RuntimeException':
        """public static java.lang.RuntimeException com.google.gson.internal.reflect.ReflectionHelper.createExceptionForUnexpectedIllegalAccess(java.lang.IllegalAccessException)"""
        return RuntimeException._wrap(_ReflectionHelper.createExceptionForUnexpectedIllegalAccess(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.internal.reflect.ReflectionHelper
from builtins import str
import com.google.gson.internal.reflect.ReflectionHelper as _ReflectionHelper
_ReflectionHelper = _ReflectionHelper
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.Field as Field
import java.lang.reflect.Method as _Method
_Method = _Method
import java.lang.String as _String
_String = _String
import java.lang.IllegalAccessException as IllegalAccessException
from typing import List
import java.lang.reflect.Constructor as _Constructor
_Constructor = _Constructor
import java.lang.RuntimeException as _RuntimeException
_RuntimeException = _RuntimeException
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import java.lang.RuntimeException as RuntimeException
import java.lang.reflect.AccessibleObject as AccessibleObject
from builtins import bool
import java.lang.Long as _long
import java.lang.reflect.Method as Method
import java.lang.reflect.Constructor as Constructor
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReflectionHelper():
    """com.google.gson.internal.reflect.ReflectionHelper"""
 
    @staticmethod
    def _wrap(java_value: _ReflectionHelper) -> 'ReflectionHelper':
        return ReflectionHelper(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectionHelper):
        """
        Dynamic initializer for ReflectionHelper.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectionHelper__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectionHelper__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def tryMakeAccessible(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.tryMakeAccessible(java.lang.reflect.Constructor<?>)"""
        return str._wrap(_ReflectionHelper.tryMakeAccessible(arg0))

    @staticmethod
    @overload
    def getRecordComponentNames(arg0: 'Class') -> List[str]:
        """public static java.lang.String[] com.google.gson.internal.reflect.ReflectionHelper.getRecordComponentNames(java.lang.Class<?>)"""
        return List[str]._wrap(_ReflectionHelper.getRecordComponentNames(arg0))

    @staticmethod
    @overload
    def fieldToString(arg0: 'Field') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.fieldToString(java.lang.reflect.Field)"""
        return str._wrap(_ReflectionHelper.fieldToString(arg0))

    @staticmethod
    @overload
    def constructorToString(arg0: 'Constructor') -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.constructorToString(java.lang.reflect.Constructor<?>)"""
        return str._wrap(_ReflectionHelper.constructorToString(arg0))

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

    @staticmethod
    @overload
    def getAccessibleObjectDescription(arg0: 'AccessibleObject', arg1: bool) -> str:
        """public static java.lang.String com.google.gson.internal.reflect.ReflectionHelper.getAccessibleObjectDescription(java.lang.reflect.AccessibleObject,boolean)"""
        return str._wrap(_ReflectionHelper.getAccessibleObjectDescription(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def makeAccessible(arg0: 'AccessibleObject'):
        """public static void com.google.gson.internal.reflect.ReflectionHelper.makeAccessible(java.lang.reflect.AccessibleObject) throws com.google.gson.JsonIOException"""
        _ReflectionHelper.makeAccessible(arg0)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getCanonicalRecordConstructor(arg0: 'Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> com.google.gson.internal.reflect.ReflectionHelper.getCanonicalRecordConstructor(java.lang.Class<T>)"""
        return Constructor._wrap(_ReflectionHelper.getCanonicalRecordConstructor(arg0))

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

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getAccessor(arg0: 'Class', arg1: 'Field') -> 'Method':
        """public static java.lang.reflect.Method com.google.gson.internal.reflect.ReflectionHelper.getAccessor(java.lang.Class<?>,java.lang.reflect.Field)"""
        return Method._wrap(_ReflectionHelper.getAccessor(arg0, arg1))

    @staticmethod
    @overload
    def isRecord(arg0: 'Class') -> bool:
        """public static boolean com.google.gson.internal.reflect.ReflectionHelper.isRecord(java.lang.Class<?>)"""
        return bool._wrap(_ReflectionHelper.isRecord(arg0))

    @staticmethod
    @overload
    def createExceptionForUnexpectedIllegalAccess(arg0: 'IllegalAccessException') -> 'RuntimeException':
        """public static java.lang.RuntimeException com.google.gson.internal.reflect.ReflectionHelper.createExceptionForUnexpectedIllegalAccess(java.lang.IllegalAccessException)"""
        return RuntimeException._wrap(_ReflectionHelper.createExceptionForUnexpectedIllegalAccess(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: com.google.gson.internal.reflect.ReflectionHelper