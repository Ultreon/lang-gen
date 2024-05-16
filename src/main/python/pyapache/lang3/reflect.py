from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.reflect.Constructor as _Constructor
_Constructor = _Constructor
import java.lang.Integer as _int
import org.apache.commons.lang3.reflect.ConstructorUtils as _ConstructorUtils
_ConstructorUtils = _ConstructorUtils
from builtins import bool
import java.lang.Long as _long
import java.lang.reflect.Constructor as Constructor
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstructorUtils():
    """org.apache.commons.lang3.reflect.ConstructorUtils"""
 
    @staticmethod
    def _wrap(java_value: _ConstructorUtils) -> 'ConstructorUtils':
        return ConstructorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstructorUtils):
        """
        Dynamic initializer for ConstructorUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstructorUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstructorUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def invokeExactConstructor(arg0: 'Class', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeExactConstructor(java.lang.Class<T>,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeExactConstructor(arg0, arg1))

    @staticmethod
    @overload
    def getAccessibleConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getAccessibleConstructor(java.lang.Class<T>,java.lang.Class<?>...)"""
        return Constructor._wrap(_ConstructorUtils.getAccessibleConstructor(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def invokeConstructor(arg0: 'Class', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeConstructor(java.lang.Class<T>,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeConstructor(arg0, arg1))

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getMatchingAccessibleConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getMatchingAccessibleConstructor(java.lang.Class<T>,java.lang.Class<?>...)"""
        return Constructor._wrap(_ConstructorUtils.getMatchingAccessibleConstructor(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.ConstructorUtils()"""
        val = _ConstructorUtils()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.ConstructorUtils()"""
        val = _ConstructorUtils()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def invokeConstructor(arg0: 'Class', arg1: 'Object', arg2: 'Class') -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeConstructor(java.lang.Class<T>,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeConstructor(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokeExactConstructor(arg0: 'Class', arg1: 'Object', arg2: 'Class') -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeExactConstructor(java.lang.Class<T>,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeExactConstructor(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getAccessibleConstructor(arg0: 'Constructor') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getAccessibleConstructor(java.lang.reflect.Constructor<T>)"""
        return Constructor._wrap(_ConstructorUtils.getAccessibleConstructor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.reflect.ConstructorUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.reflect.Constructor as _Constructor
_Constructor = _Constructor
import java.lang.Integer as _int
import org.apache.commons.lang3.reflect.ConstructorUtils as _ConstructorUtils
_ConstructorUtils = _ConstructorUtils
from builtins import bool
import java.lang.Long as _long
import java.lang.reflect.Constructor as Constructor
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ConstructorUtils():
    """org.apache.commons.lang3.reflect.ConstructorUtils"""
 
    @staticmethod
    def _wrap(java_value: _ConstructorUtils) -> 'ConstructorUtils':
        return ConstructorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ConstructorUtils):
        """
        Dynamic initializer for ConstructorUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ConstructorUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ConstructorUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def invokeExactConstructor(arg0: 'Class', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeExactConstructor(java.lang.Class<T>,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeExactConstructor(arg0, arg1))

    @staticmethod
    @overload
    def getAccessibleConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getAccessibleConstructor(java.lang.Class<T>,java.lang.Class<?>...)"""
        return Constructor._wrap(_ConstructorUtils.getAccessibleConstructor(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def invokeConstructor(arg0: 'Class', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeConstructor(java.lang.Class<T>,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeConstructor(arg0, arg1))

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getMatchingAccessibleConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getMatchingAccessibleConstructor(java.lang.Class<T>,java.lang.Class<?>...)"""
        return Constructor._wrap(_ConstructorUtils.getMatchingAccessibleConstructor(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.ConstructorUtils()"""
        val = _ConstructorUtils()
        self.__wrapper = val

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.ConstructorUtils()"""
        val = _ConstructorUtils()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def invokeConstructor(arg0: 'Class', arg1: 'Object', arg2: 'Class') -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeConstructor(java.lang.Class<T>,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeConstructor(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokeExactConstructor(arg0: 'Class', arg1: 'Object', arg2: 'Class') -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeExactConstructor(java.lang.Class<T>,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object._wrap(_ConstructorUtils.invokeExactConstructor(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getAccessibleConstructor(arg0: 'Constructor') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getAccessibleConstructor(java.lang.reflect.Constructor<T>)"""
        return Constructor._wrap(_ConstructorUtils.getAccessibleConstructor(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())

 
 
 
# CLASS: org.apache.commons.lang3.reflect.ConstructorUtils 
 
 
# CLASS: org.apache.commons.lang3.reflect.TypeUtils
import java.lang.reflect.GenericArrayType as GenericArrayType
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.util.Map as _Map
_Map = _Map
import java.lang.reflect.ParameterizedType as ParameterizedType
import java.lang.reflect.Type as Type
from builtins import bool
from builtins import str
import org.apache.commons.lang3.reflect.Typed as _Typed
_Typed = _Typed
import java.lang.reflect.WildcardType as WildcardType
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.reflect.Type as _Type
_Type = _Type
import java.lang.reflect.GenericArrayType as _GenericArrayType
_GenericArrayType = _GenericArrayType
from typing import List
import org.apache.commons.lang3.reflect.TypeUtils as _TypeUtils_WildcardTypeBuilder
_WildcardTypeBuilder = _TypeUtils_WildcardTypeBuilder.WildcardTypeBuilder
import java.lang.Integer as _int
import java.lang.reflect.TypeVariable as TypeVariable
import java.util.Map as Map
import java.lang.reflect.ParameterizedType as _ParameterizedType
_ParameterizedType = _ParameterizedType
import java.lang.Long as _long
import org.apache.commons.lang3.reflect.TypeUtils as _TypeUtils
_TypeUtils = _TypeUtils
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class TypeUtils():
    """org.apache.commons.lang3.reflect.TypeUtils"""
 
    @staticmethod
    def _wrap(java_value: _TypeUtils) -> 'TypeUtils':
        return TypeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeUtils):
        """
        Dynamic initializer for TypeUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isArrayType(arg0: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isArrayType(java.lang.reflect.Type)"""
        return bool._wrap(_TypeUtils.isArrayType(arg0))

    @staticmethod
    @overload
    def parameterizeWithOwner(arg0: 'Type', arg1: 'Class', *arg2: 'Type') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterizeWithOwner(java.lang.reflect.Type,java.lang.Class<?>,java.lang.reflect.Type...)"""
        return ParameterizedType._wrap(_TypeUtils.parameterizeWithOwner(arg0, arg1, arg2))

    @staticmethod
    @overload
    def equals(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.equals(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool._wrap(_TypeUtils.equals(arg0, arg1))

    @staticmethod
    @overload
    def wildcardType() -> 'WildcardTypeBuilder':
        """public static org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder org.apache.commons.lang3.reflect.TypeUtils.wildcardType()"""
        return WildcardTypeBuilder._wrap(_TypeUtils.wildcardType())

    @staticmethod
    @overload
    def getImplicitLowerBounds(arg0: 'WildcardType') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitLowerBounds(java.lang.reflect.WildcardType)"""
        return List[Type]._wrap(_TypeUtils.getImplicitLowerBounds(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getRawType(arg0: 'Type', arg1: 'Type') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.reflect.TypeUtils.getRawType(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return type.Class._wrap(_TypeUtils.getRawType(arg0, arg1))

    @staticmethod
    @overload
    def parameterize(arg0: 'Class', *arg1: 'Type') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterize(java.lang.Class<?>,java.lang.reflect.Type...)"""
        return ParameterizedType._wrap(_TypeUtils.parameterize(arg0, arg1))

    @staticmethod
    @overload
    def normalizeUpperBounds(arg0: 'Type') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.normalizeUpperBounds(java.lang.reflect.Type[])"""
        return List[Type]._wrap(_TypeUtils.normalizeUpperBounds(arg0))

    @staticmethod
    @overload
    def containsTypeVariables(arg0: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.containsTypeVariables(java.lang.reflect.Type)"""
        return bool._wrap(_TypeUtils.containsTypeVariables(arg0))

    @staticmethod
    @overload
    def wrap(arg0: 'Type') -> 'Typed':
        """public static <T> org.apache.commons.lang3.reflect.Typed<T> org.apache.commons.lang3.reflect.TypeUtils.wrap(java.lang.reflect.Type)"""
        return Typed._wrap(_TypeUtils.wrap(arg0))

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
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.TypeUtils()"""
        val = _TypeUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def wrap(arg0: 'Class') -> 'Typed':
        """public static <T> org.apache.commons.lang3.reflect.Typed<T> org.apache.commons.lang3.reflect.TypeUtils.wrap(java.lang.Class<T>)"""
        return Typed._wrap(_TypeUtils.wrap(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isAssignable(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool._wrap(_TypeUtils.isAssignable(arg0, arg1))

    @staticmethod
    @overload
    def genericArrayType(arg0: 'Type') -> 'GenericArrayType':
        """public static java.lang.reflect.GenericArrayType org.apache.commons.lang3.reflect.TypeUtils.genericArrayType(java.lang.reflect.Type)"""
        return GenericArrayType._wrap(_TypeUtils.genericArrayType(arg0))

    @staticmethod
    @overload
    def getImplicitUpperBounds(arg0: 'WildcardType') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitUpperBounds(java.lang.reflect.WildcardType)"""
        return List[Type]._wrap(_TypeUtils.getImplicitUpperBounds(arg0))

    @staticmethod
    @overload
    def determineTypeArguments(arg0: 'Class', arg1: 'ParameterizedType') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.determineTypeArguments(java.lang.Class<?>,java.lang.reflect.ParameterizedType)"""
        return Map._wrap(_TypeUtils.determineTypeArguments(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def isInstance(arg0: object, arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isInstance(java.lang.Object,java.lang.reflect.Type)"""
        return bool._wrap(_TypeUtils.isInstance(arg0, arg1))

    @staticmethod
    @overload
    def getImplicitBounds(arg0: 'TypeVariable') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitBounds(java.lang.reflect.TypeVariable<?>)"""
        return List[Type]._wrap(_TypeUtils.getImplicitBounds(arg0))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.TypeUtils()"""
        val = _TypeUtils()
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def toString(arg0: 'Type') -> str:
        """public static java.lang.String org.apache.commons.lang3.reflect.TypeUtils.toString(java.lang.reflect.Type)"""
        return str._wrap(_TypeUtils.toString(arg0))

    @staticmethod
    @overload
    def toLongString(arg0: 'TypeVariable') -> str:
        """public static java.lang.String org.apache.commons.lang3.reflect.TypeUtils.toLongString(java.lang.reflect.TypeVariable<?>)"""
        return str._wrap(_TypeUtils.toLongString(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def unrollVariables(arg0: 'Map', arg1: 'Type') -> 'Type':
        """public static java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeUtils.unrollVariables(java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>,java.lang.reflect.Type)"""
        return Type._wrap(_TypeUtils.unrollVariables(arg0, arg1))

    @staticmethod
    @overload
    def parameterize(arg0: 'Class', arg1: 'Map') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterize(java.lang.Class<?>,java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return ParameterizedType._wrap(_TypeUtils.parameterize(arg0, arg1))

    @staticmethod
    @overload
    def parameterizeWithOwner(arg0: 'Type', arg1: 'Class', arg2: 'Map') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterizeWithOwner(java.lang.reflect.Type,java.lang.Class<?>,java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return ParameterizedType._wrap(_TypeUtils.parameterizeWithOwner(arg0, arg1, arg2))

    @staticmethod
    @overload
    def typesSatisfyVariables(arg0: 'Map') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.typesSatisfyVariables(java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return bool._wrap(_TypeUtils.typesSatisfyVariables(arg0))

    @staticmethod
    @overload
    def getTypeArguments(arg0: 'ParameterizedType') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.getTypeArguments(java.lang.reflect.ParameterizedType)"""
        return Map._wrap(_TypeUtils.getTypeArguments(arg0))

    @staticmethod
    @overload
    def getTypeArguments(arg0: 'Type', arg1: 'Class') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.getTypeArguments(java.lang.reflect.Type,java.lang.Class<?>)"""
        return Map._wrap(_TypeUtils.getTypeArguments(arg0, arg1))

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
    def getArrayComponentType(arg0: 'Type') -> 'Type':
        """public static java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeUtils.getArrayComponentType(java.lang.reflect.Type)"""
        return Type._wrap(_TypeUtils.getArrayComponentType(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.reflect.InheritanceUtils
from builtins import str
from pyquantum_helper import override
import org.apache.commons.lang3.reflect.InheritanceUtils as _InheritanceUtils
_InheritanceUtils = _InheritanceUtils
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class InheritanceUtils():
    """org.apache.commons.lang3.reflect.InheritanceUtils"""
 
    @staticmethod
    def _wrap(java_value: _InheritanceUtils) -> 'InheritanceUtils':
        return InheritanceUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _InheritanceUtils):
        """
        Dynamic initializer for InheritanceUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_InheritanceUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_InheritanceUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.InheritanceUtils()"""
        val = _InheritanceUtils()
        self.__wrapper = val

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

    @staticmethod
    @overload
    def distance(arg0: 'Class', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.reflect.InheritanceUtils.distance(java.lang.Class<?>,java.lang.Class<?>)"""
        return int._wrap(_InheritanceUtils.distance(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.InheritanceUtils()"""
        val = _InheritanceUtils()
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.reflect.FieldUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.reflect.Field as Field
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
import org.apache.commons.lang3.reflect.FieldUtils as _FieldUtils
_FieldUtils = _FieldUtils
from typing import List
import java.lang.String as _string
import java.lang.reflect.Field as _Field
_Field = _Field
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class FieldUtils():
    """org.apache.commons.lang3.reflect.FieldUtils"""
 
    @staticmethod
    def _wrap(java_value: _FieldUtils) -> 'FieldUtils':
        return FieldUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _FieldUtils):
        """
        Dynamic initializer for FieldUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_FieldUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_FieldUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def writeDeclaredStaticField(arg0: 'Class', arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeDeclaredStaticField(arg0, arg1, arg2)

    @staticmethod
    @overload
    def writeField(arg0: 'Field', arg1: object, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.reflect.Field,java.lang.Object,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeField(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @staticmethod
    @overload
    def readStaticField(arg0: 'Field', arg1: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.reflect.Field,boolean) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readStaticField(arg0, _boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Field', arg1: object, arg2: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.reflect.Field,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeStaticField(arg0, arg1, _boolean.valueOf(arg2))

    @staticmethod
    @overload
    def removeFinalModifier(arg0: 'Field', arg1: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.removeFinalModifier(java.lang.reflect.Field,boolean)"""
        _FieldUtils.removeFinalModifier(arg0, _boolean.valueOf(arg1))

    @staticmethod
    @overload
    def readField(arg0: 'Field', arg1: object, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.reflect.Field,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readField(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def writeDeclaredStaticField(arg0: 'Class', arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeDeclaredStaticField(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @staticmethod
    @overload
    def writeField(arg0: 'Field', arg1: object, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.reflect.Field,java.lang.Object,java.lang.Object) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeField(arg0, arg1, arg2)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def readStaticField(arg0: 'Field') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.reflect.Field) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readStaticField(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Field', arg1: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.reflect.Field,java.lang.Object) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeStaticField(arg0, arg1)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getField(arg0: 'Class', arg1: str) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getField(java.lang.Class<?>,java.lang.String)"""
        return Field._wrap(_FieldUtils.getField(arg0, arg1))

    @staticmethod
    @overload
    def writeDeclaredField(arg0: object, arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredField(java.lang.Object,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeDeclaredField(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Class', arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeStaticField(arg0, arg1, arg2)

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def readDeclaredField(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredField(java.lang.Object,java.lang.String) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readDeclaredField(arg0, arg1))

    @staticmethod
    @overload
    def readField(arg0: object, arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.Object,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readField(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def readDeclaredStaticField(arg0: 'Class', arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredStaticField(java.lang.Class<?>,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readDeclaredStaticField(arg0, arg1, _boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.FieldUtils()"""
        val = _FieldUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def writeDeclaredField(arg0: object, arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredField(java.lang.Object,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeDeclaredField(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getAllFields(arg0: 'Class') -> List['Field']:
        """public static java.lang.reflect.Field[] org.apache.commons.lang3.reflect.FieldUtils.getAllFields(java.lang.Class<?>)"""
        return List[Field]._wrap(_FieldUtils.getAllFields(arg0))

    @staticmethod
    @overload
    def getFieldsListWithAnnotation(arg0: 'Class', arg1: 'Class') -> 'List':
        """public static java.util.List<java.lang.reflect.Field> org.apache.commons.lang3.reflect.FieldUtils.getFieldsListWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List._wrap(_FieldUtils.getFieldsListWithAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def readStaticField(arg0: 'Class', arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.Class<?>,java.lang.String) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readStaticField(arg0, arg1))

    @staticmethod
    @overload
    def readDeclaredStaticField(arg0: 'Class', arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredStaticField(java.lang.Class<?>,java.lang.String) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readDeclaredStaticField(arg0, arg1))

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Class', arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeStaticField(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @staticmethod
    @overload
    def writeField(arg0: object, arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.Object,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeField(arg0, arg1, arg2, _boolean.valueOf(arg3))

    @staticmethod
    @overload
    def getAllFieldsList(arg0: 'Class') -> 'List':
        """public static java.util.List<java.lang.reflect.Field> org.apache.commons.lang3.reflect.FieldUtils.getAllFieldsList(java.lang.Class<?>)"""
        return List._wrap(_FieldUtils.getAllFieldsList(arg0))

    @staticmethod
    @overload
    def removeFinalModifier(arg0: 'Field'):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.removeFinalModifier(java.lang.reflect.Field)"""
        _FieldUtils.removeFinalModifier(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getFieldsWithAnnotation(arg0: 'Class', arg1: 'Class') -> List['Field']:
        """public static java.lang.reflect.Field[] org.apache.commons.lang3.reflect.FieldUtils.getFieldsWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List[Field]._wrap(_FieldUtils.getFieldsWithAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def writeField(arg0: object, arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.Object,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        _FieldUtils.writeField(arg0, arg1, arg2)

    @staticmethod
    @overload
    def getDeclaredField(arg0: 'Class', arg1: str) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getDeclaredField(java.lang.Class<?>,java.lang.String)"""
        return Field._wrap(_FieldUtils.getDeclaredField(arg0, arg1))

    @staticmethod
    @overload
    def readStaticField(arg0: 'Class', arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.Class<?>,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readStaticField(arg0, arg1, _boolean.valueOf(arg2)))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.FieldUtils()"""
        val = _FieldUtils()
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def readField(arg0: 'Field', arg1: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.reflect.Field,java.lang.Object) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readField(arg0, arg1))

    @staticmethod
    @overload
    def readField(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.Object,java.lang.String) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readField(arg0, arg1))

    @staticmethod
    @overload
    def readDeclaredField(arg0: object, arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredField(java.lang.Object,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object._wrap(_FieldUtils.readDeclaredField(arg0, arg1, _boolean.valueOf(arg2)))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getField(arg0: 'Class', arg1: str, arg2: bool) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getField(java.lang.Class<?>,java.lang.String,boolean)"""
        return Field._wrap(_FieldUtils.getField(arg0, arg1, _boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def getDeclaredField(arg0: 'Class', arg1: str, arg2: bool) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getDeclaredField(java.lang.Class<?>,java.lang.String,boolean)"""
        return Field._wrap(_FieldUtils.getDeclaredField(arg0, arg1, _boolean.valueOf(arg2)))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.reflect.MethodUtils
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import org.apache.commons.lang3.reflect.MethodUtils as _MethodUtils
_MethodUtils = _MethodUtils
import java.lang.annotation.Annotation as Annotation
import java.util.Set as _Set
_Set = _Set
import java.lang.String as _string
import java.lang.Boolean as _boolean
from builtins import bool
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import java.lang.reflect.Method as _Method
_Method = _Method
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.List as _List
_List = _List
from typing import List
import java.util.Set as Set
import java.lang.Integer as _int
try:
    from pyapache import lang3
except ImportError:
    lang3 = _import_once("pyapache.lang3")

import java.lang.Long as _long
import java.lang.reflect.Method as Method
import java.util.List as List
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MethodUtils():
    """org.apache.commons.lang3.reflect.MethodUtils"""
 
    @staticmethod
    def _wrap(java_value: _MethodUtils) -> 'MethodUtils':
        return MethodUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MethodUtils):
        """
        Dynamic initializer for MethodUtils.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MethodUtils__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MethodUtils__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getOverrideHierarchy(arg0: 'Method', arg1: 'Interfaces') -> 'Set':
        """public static java.util.Set<java.lang.reflect.Method> org.apache.commons.lang3.reflect.MethodUtils.getOverrideHierarchy(java.lang.reflect.Method,org.apache.commons.lang3.ClassUtils$Interfaces)"""
        return Set._wrap(_MethodUtils.getOverrideHierarchy(arg0, arg1))

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokeExactMethod(arg0: object, arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactMethod(java.lang.Object,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeExactMethod(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def getMatchingAccessibleMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getMatchingAccessibleMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...)"""
        return Method._wrap(_MethodUtils.getMatchingAccessibleMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokeExactStaticMethod(arg0: 'Class', arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeExactStaticMethod(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: bool, arg2: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,boolean,java.lang.String) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeMethod(arg0, _boolean.valueOf(arg1), arg2))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.MethodUtils()"""
        val = _MethodUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def invokeStaticMethod(arg0: 'Class', arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeStaticMethod(arg0, arg1, arg2, arg3))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.MethodUtils()"""
        val = _MethodUtils()
        self.__wrapper = val

    @staticmethod
    @overload
    def invokeExactMethod(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactMethod(java.lang.Object,java.lang.String) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeExactMethod(arg0, arg1))

    @staticmethod
    @overload
    def getMethodsWithAnnotation(arg0: 'Class', arg1: 'Class', arg2: bool, arg3: bool) -> List['Method']:
        """public static java.lang.reflect.Method[] org.apache.commons.lang3.reflect.MethodUtils.getMethodsWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>,boolean,boolean)"""
        return List[Method]._wrap(_MethodUtils.getMethodsWithAnnotation(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getMethodsListWithAnnotation(arg0: 'Class', arg1: 'Class', arg2: bool, arg3: bool) -> 'List':
        """public static java.util.List<java.lang.reflect.Method> org.apache.commons.lang3.reflect.MethodUtils.getMethodsListWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>,boolean,boolean)"""
        return List._wrap(_MethodUtils.getMethodsListWithAnnotation(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,java.lang.String) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeMethod(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def invokeStaticMethod(arg0: 'Class', arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeStaticMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getMatchingMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getMatchingMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...)"""
        return Method._wrap(_MethodUtils.getMatchingMethod(arg0, arg1, arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeMethod(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def invokeExactStaticMethod(arg0: 'Class', arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeExactStaticMethod(arg0, arg1, arg2, arg3))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getAccessibleMethod(arg0: 'Method') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getAccessibleMethod(java.lang.reflect.Method)"""
        return Method._wrap(_MethodUtils.getAccessibleMethod(arg0))

    @staticmethod
    @overload
    def getMethodsListWithAnnotation(arg0: 'Class', arg1: 'Class') -> 'List':
        """public static java.util.List<java.lang.reflect.Method> org.apache.commons.lang3.reflect.MethodUtils.getMethodsListWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List._wrap(_MethodUtils.getMethodsListWithAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def getAnnotation(arg0: 'Method', arg1: 'Class', arg2: bool, arg3: bool) -> 'Annotation':
        """public static <A extends java.lang.annotation.Annotation> A org.apache.commons.lang3.reflect.MethodUtils.getAnnotation(java.lang.reflect.Method,java.lang.Class<A>,boolean,boolean)"""
        return Annotation._wrap(_MethodUtils.getAnnotation(arg0, arg1, _boolean.valueOf(arg2), _boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeExactMethod(arg0: object, arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactMethod(java.lang.Object,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeExactMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: bool, arg2: str, arg3: 'Object', arg4: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,boolean,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeMethod(arg0, _boolean.valueOf(arg1), arg2, arg3, arg4))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getAccessibleMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getAccessibleMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...)"""
        return Method._wrap(_MethodUtils.getAccessibleMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getMethodsWithAnnotation(arg0: 'Class', arg1: 'Class') -> List['Method']:
        """public static java.lang.reflect.Method[] org.apache.commons.lang3.reflect.MethodUtils.getMethodsWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List[Method]._wrap(_MethodUtils.getMethodsWithAnnotation(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: bool, arg2: str, *arg3: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,boolean,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object._wrap(_MethodUtils.invokeMethod(arg0, _boolean.valueOf(arg1), arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder
from builtins import str
import java.lang.reflect.WildcardType as WildcardType
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.reflect.WildcardType as _WildcardType
_WildcardType = _WildcardType
import org.apache.commons.lang3.reflect.TypeUtils as _TypeUtils_WildcardTypeBuilder
_WildcardTypeBuilder = _TypeUtils_WildcardTypeBuilder.WildcardTypeBuilder
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class WildcardTypeBuilder():
    """org.apache.commons.lang3.reflect.TypeUtils.WildcardTypeBuilder"""
 
    @staticmethod
    def _wrap(java_value: _WildcardTypeBuilder) -> 'WildcardTypeBuilder':
        return WildcardTypeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _WildcardTypeBuilder):
        """
        Dynamic initializer for WildcardTypeBuilder.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_WildcardTypeBuilder__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_WildcardTypeBuilder__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def withLowerBounds(self, *arg0: 'Type') -> 'WildcardTypeBuilder':
        """public org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder.withLowerBounds(java.lang.reflect.Type...)"""
        return 'WildcardTypeBuilder'._wrap(super(_WildcardTypeBuilder, self).withLowerBounds(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def withUpperBounds(self, *arg0: 'Type') -> 'WildcardTypeBuilder':
        """public org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder.withUpperBounds(java.lang.reflect.Type...)"""
        return 'WildcardTypeBuilder'._wrap(super(_WildcardTypeBuilder, self).withUpperBounds(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def build(self) -> 'WildcardType':
        """public java.lang.reflect.WildcardType org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder.build()"""
        return 'WildcardType'._wrap(super(WildcardTypeBuilder, self).build())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: org.apache.commons.lang3.reflect.TypeLiteral
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import org.apache.commons.lang3.reflect.TypeLiteral as _TypeLiteral
_TypeLiteral = _TypeLiteral
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.reflect.Type as _Type
_Type = _Type
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TypeLiteral():
    """org.apache.commons.lang3.reflect.TypeLiteral"""
 
    @staticmethod
    def _wrap(java_value: _TypeLiteral) -> 'TypeLiteral':
        return TypeLiteral(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeLiteral):
        """
        Dynamic initializer for TypeLiteral.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeLiteral__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeLiteral__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
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
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.reflect.TypeLiteral.hashCode()"""
        return int._wrap(super(TypeLiteral, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean org.apache.commons.lang3.reflect.TypeLiteral.equals(java.lang.Object)"""
        return bool._wrap(super(_TypeLiteral, self).equals(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

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
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String org.apache.commons.lang3.reflect.TypeLiteral.toString()"""
        return str._wrap(super(TypeLiteral, self).toString())

    @override
    @overload
    def getType(self) -> 'Type':
        """public java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeLiteral.getType()"""
        return 'Type'._wrap(super(TypeLiteral, self).getType()) 
 
 
# CLASS: org.apache.commons.lang3.reflect.Typed
import org.apache.commons.lang3.reflect.Typed as _Typed
_Typed = _Typed
from abc import abstractmethod, ABC
 
class Typed():
    """org.apache.commons.lang3.reflect.Typed"""
 
    @staticmethod
    def _wrap(java_value: _Typed) -> 'Typed':
        return Typed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Typed):
        """
        Dynamic initializer for Typed.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Typed__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Typed__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getType(self, ):
        """public abstract java.lang.reflect.Type org.apache.commons.lang3.reflect.Typed.getType()"""
        pass