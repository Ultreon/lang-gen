from __future__ import annotations
from overload import overload


 
import java.lang.reflect.GenericArrayType as GenericArrayType
import java.lang.reflect.GenericArrayType as __GenericArrayType
__GenericArrayType = __GenericArrayType
from builtins import type
import java.lang.reflect.ParameterizedType as ParameterizedType
import java.util.Map as __Map
__Map = __Map
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.reflect.TypeUtils as __TypeUtils
__TypeUtils = __TypeUtils
import org.apache.commons.lang3.reflect.Typed as __Typed
__Typed = __Typed
from builtins import bool
from builtins import str
import java.lang.reflect.WildcardType as WildcardType
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.reflect.TypeUtils as __TypeUtils_WildcardTypeBuilder
__WildcardTypeBuilder = __TypeUtils_WildcardTypeBuilder.WildcardTypeBuilder
import java.lang.reflect.ParameterizedType as __ParameterizedType
__ParameterizedType = __ParameterizedType
from typing import List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.reflect.TypeVariable as TypeVariable
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class TypeUtils():
    """org.apache.commons.lang3.reflect.TypeUtils"""
 
    @staticmethod
    def __wrap(java_value: __TypeUtils) -> 'TypeUtils':
        return TypeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeUtils):
        """
        Dynamic initializer for TypeUtils.
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

    @staticmethod
    @overload
    def toString(arg0: 'Type') -> str:
        """public static java.lang.String org.apache.commons.lang3.reflect.TypeUtils.toString(java.lang.reflect.Type)"""
        return str.__wrap(__TypeUtils.toString(arg0))

    @staticmethod
    @overload
    def getImplicitUpperBounds(arg0: 'WildcardType') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitUpperBounds(java.lang.reflect.WildcardType)"""
        return List[Type].__wrap(__TypeUtils.getImplicitUpperBounds(arg0))

    @staticmethod
    @overload
    def isInstance(arg0: object, arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isInstance(java.lang.Object,java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.isInstance(arg0, arg1))

    @staticmethod
    @overload
    def getTypeArguments(arg0: 'ParameterizedType') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.getTypeArguments(java.lang.reflect.ParameterizedType)"""
        return Map.__wrap(__TypeUtils.getTypeArguments(arg0))

    @staticmethod
    @overload
    def parameterizeWithOwner(arg0: 'Type', arg1: 'Class', arg2: 'Map') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterizeWithOwner(java.lang.reflect.Type,java.lang.Class<?>,java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterizeWithOwner(arg0, arg1, arg2))

    @staticmethod
    @overload
    def unrollVariables(arg0: 'Map', arg1: 'Type') -> 'Type':
        """public static java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeUtils.unrollVariables(java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>,java.lang.reflect.Type)"""
        return Type.__wrap(__TypeUtils.unrollVariables(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getRawType(arg0: 'Type', arg1: 'Type') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.reflect.TypeUtils.getRawType(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return type.Class.__wrap(__TypeUtils.getRawType(arg0, arg1))

    @staticmethod
    @overload
    def getArrayComponentType(arg0: 'Type') -> 'Type':
        """public static java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeUtils.getArrayComponentType(java.lang.reflect.Type)"""
        return Type.__wrap(__TypeUtils.getArrayComponentType(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.TypeUtils()"""
        val = __TypeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def normalizeUpperBounds(arg0: 'Type') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.normalizeUpperBounds(java.lang.reflect.Type[])"""
        return List[Type].__wrap(__TypeUtils.normalizeUpperBounds(arg0))

    @staticmethod
    @overload
    def getImplicitLowerBounds(arg0: 'WildcardType') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitLowerBounds(java.lang.reflect.WildcardType)"""
        return List[Type].__wrap(__TypeUtils.getImplicitLowerBounds(arg0))

    @staticmethod
    @overload
    def parameterize(arg0: 'Class', *arg1: 'Type') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterize(java.lang.Class<?>,java.lang.reflect.Type...)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterize(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.TypeUtils()"""
        val = __TypeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parameterize(arg0: 'Class', arg1: 'Map') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterize(java.lang.Class<?>,java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterize(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getImplicitBounds(arg0: 'TypeVariable') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitBounds(java.lang.reflect.TypeVariable<?>)"""
        return List[Type].__wrap(__TypeUtils.getImplicitBounds(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def parameterizeWithOwner(arg0: 'Type', arg1: 'Class', *arg2: 'Type') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterizeWithOwner(java.lang.reflect.Type,java.lang.Class<?>,java.lang.reflect.Type...)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterizeWithOwner(arg0, arg1, arg2))

    @staticmethod
    @overload
    def wildcardType() -> 'WildcardTypeBuilder':
        """public static org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder org.apache.commons.lang3.reflect.TypeUtils.wildcardType()"""
        return WildcardTypeBuilder.__wrap(__TypeUtils.wildcardType())

    @staticmethod
    @overload
    def toLongString(arg0: 'TypeVariable') -> str:
        """public static java.lang.String org.apache.commons.lang3.reflect.TypeUtils.toLongString(java.lang.reflect.TypeVariable<?>)"""
        return str.__wrap(__TypeUtils.toLongString(arg0))

    @staticmethod
    @overload
    def equals(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.equals(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.equals(arg0, arg1))

    @staticmethod
    @overload
    def wrap(arg0: 'Class') -> 'Typed':
        """public static <T> org.apache.commons.lang3.reflect.Typed<T> org.apache.commons.lang3.reflect.TypeUtils.wrap(java.lang.Class<T>)"""
        return Typed.__wrap(__TypeUtils.wrap(arg0))

    @staticmethod
    @overload
    def determineTypeArguments(arg0: 'Class', arg1: 'ParameterizedType') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.determineTypeArguments(java.lang.Class<?>,java.lang.reflect.ParameterizedType)"""
        return Map.__wrap(__TypeUtils.determineTypeArguments(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def wrap(arg0: 'Type') -> 'Typed':
        """public static <T> org.apache.commons.lang3.reflect.Typed<T> org.apache.commons.lang3.reflect.TypeUtils.wrap(java.lang.reflect.Type)"""
        return Typed.__wrap(__TypeUtils.wrap(arg0))

    @staticmethod
    @overload
    def isArrayType(arg0: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isArrayType(java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.isArrayType(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @staticmethod
    @overload
    def genericArrayType(arg0: 'Type') -> 'GenericArrayType':
        """public static java.lang.reflect.GenericArrayType org.apache.commons.lang3.reflect.TypeUtils.genericArrayType(java.lang.reflect.Type)"""
        return GenericArrayType.__wrap(__TypeUtils.genericArrayType(arg0))

    @staticmethod
    @overload
    def getTypeArguments(arg0: 'Type', arg1: 'Class') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.getTypeArguments(java.lang.reflect.Type,java.lang.Class<?>)"""
        return Map.__wrap(__TypeUtils.getTypeArguments(arg0, arg1))

    @staticmethod
    @overload
    def typesSatisfyVariables(arg0: 'Map') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.typesSatisfyVariables(java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return bool.__wrap(__TypeUtils.typesSatisfyVariables(arg0))

    @staticmethod
    @overload
    def containsTypeVariables(arg0: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.containsTypeVariables(java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.containsTypeVariables(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isAssignable(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.isAssignable(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: org.apache.commons.lang3.reflect.TypeUtils
import java.lang.reflect.GenericArrayType as GenericArrayType
import java.lang.reflect.GenericArrayType as __GenericArrayType
__GenericArrayType = __GenericArrayType
from builtins import type
import java.lang.reflect.ParameterizedType as ParameterizedType
import java.util.Map as __Map
__Map = __Map
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
import java.lang.Class as __Class
__Class = __Class
import org.apache.commons.lang3.reflect.TypeUtils as __TypeUtils
__TypeUtils = __TypeUtils
import org.apache.commons.lang3.reflect.Typed as __Typed
__Typed = __Typed
from builtins import bool
from builtins import str
import java.lang.reflect.WildcardType as WildcardType
from pyquantum_helper import override
import java.lang.Object as __object
import org.apache.commons.lang3.reflect.TypeUtils as __TypeUtils_WildcardTypeBuilder
__WildcardTypeBuilder = __TypeUtils_WildcardTypeBuilder.WildcardTypeBuilder
import java.lang.reflect.ParameterizedType as __ParameterizedType
__ParameterizedType = __ParameterizedType
from typing import List
import java.lang.Long as __long
import java.lang.String as __String
__String = __String
import java.lang.reflect.TypeVariable as TypeVariable
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.util.Map as Map
from builtins import int
 
class TypeUtils():
    """org.apache.commons.lang3.reflect.TypeUtils"""
 
    @staticmethod
    def __wrap(java_value: __TypeUtils) -> 'TypeUtils':
        return TypeUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeUtils):
        """
        Dynamic initializer for TypeUtils.
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

    @staticmethod
    @overload
    def toString(arg0: 'Type') -> str:
        """public static java.lang.String org.apache.commons.lang3.reflect.TypeUtils.toString(java.lang.reflect.Type)"""
        return str.__wrap(__TypeUtils.toString(arg0))

    @staticmethod
    @overload
    def getImplicitUpperBounds(arg0: 'WildcardType') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitUpperBounds(java.lang.reflect.WildcardType)"""
        return List[Type].__wrap(__TypeUtils.getImplicitUpperBounds(arg0))

    @staticmethod
    @overload
    def isInstance(arg0: object, arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isInstance(java.lang.Object,java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.isInstance(arg0, arg1))

    @staticmethod
    @overload
    def getTypeArguments(arg0: 'ParameterizedType') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.getTypeArguments(java.lang.reflect.ParameterizedType)"""
        return Map.__wrap(__TypeUtils.getTypeArguments(arg0))

    @staticmethod
    @overload
    def parameterizeWithOwner(arg0: 'Type', arg1: 'Class', arg2: 'Map') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterizeWithOwner(java.lang.reflect.Type,java.lang.Class<?>,java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterizeWithOwner(arg0, arg1, arg2))

    @staticmethod
    @overload
    def unrollVariables(arg0: 'Map', arg1: 'Type') -> 'Type':
        """public static java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeUtils.unrollVariables(java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>,java.lang.reflect.Type)"""
        return Type.__wrap(__TypeUtils.unrollVariables(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getRawType(arg0: 'Type', arg1: 'Type') -> 'type.Class':
        """public static java.lang.Class<?> org.apache.commons.lang3.reflect.TypeUtils.getRawType(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return type.Class.__wrap(__TypeUtils.getRawType(arg0, arg1))

    @staticmethod
    @overload
    def getArrayComponentType(arg0: 'Type') -> 'Type':
        """public static java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeUtils.getArrayComponentType(java.lang.reflect.Type)"""
        return Type.__wrap(__TypeUtils.getArrayComponentType(arg0))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.TypeUtils()"""
        val = __TypeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def normalizeUpperBounds(arg0: 'Type') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.normalizeUpperBounds(java.lang.reflect.Type[])"""
        return List[Type].__wrap(__TypeUtils.normalizeUpperBounds(arg0))

    @staticmethod
    @overload
    def getImplicitLowerBounds(arg0: 'WildcardType') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitLowerBounds(java.lang.reflect.WildcardType)"""
        return List[Type].__wrap(__TypeUtils.getImplicitLowerBounds(arg0))

    @staticmethod
    @overload
    def parameterize(arg0: 'Class', *arg1: 'Type') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterize(java.lang.Class<?>,java.lang.reflect.Type...)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterize(arg0, arg1))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.TypeUtils()"""
        val = __TypeUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def parameterize(arg0: 'Class', arg1: 'Map') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterize(java.lang.Class<?>,java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterize(arg0, arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getImplicitBounds(arg0: 'TypeVariable') -> List['Type']:
        """public static java.lang.reflect.Type[] org.apache.commons.lang3.reflect.TypeUtils.getImplicitBounds(java.lang.reflect.TypeVariable<?>)"""
        return List[Type].__wrap(__TypeUtils.getImplicitBounds(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def parameterizeWithOwner(arg0: 'Type', arg1: 'Class', *arg2: 'Type') -> 'ParameterizedType':
        """public static final java.lang.reflect.ParameterizedType org.apache.commons.lang3.reflect.TypeUtils.parameterizeWithOwner(java.lang.reflect.Type,java.lang.Class<?>,java.lang.reflect.Type...)"""
        return ParameterizedType.__wrap(__TypeUtils.parameterizeWithOwner(arg0, arg1, arg2))

    @staticmethod
    @overload
    def wildcardType() -> 'WildcardTypeBuilder':
        """public static org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder org.apache.commons.lang3.reflect.TypeUtils.wildcardType()"""
        return WildcardTypeBuilder.__wrap(__TypeUtils.wildcardType())

    @staticmethod
    @overload
    def toLongString(arg0: 'TypeVariable') -> str:
        """public static java.lang.String org.apache.commons.lang3.reflect.TypeUtils.toLongString(java.lang.reflect.TypeVariable<?>)"""
        return str.__wrap(__TypeUtils.toLongString(arg0))

    @staticmethod
    @overload
    def equals(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.equals(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.equals(arg0, arg1))

    @staticmethod
    @overload
    def wrap(arg0: 'Class') -> 'Typed':
        """public static <T> org.apache.commons.lang3.reflect.Typed<T> org.apache.commons.lang3.reflect.TypeUtils.wrap(java.lang.Class<T>)"""
        return Typed.__wrap(__TypeUtils.wrap(arg0))

    @staticmethod
    @overload
    def determineTypeArguments(arg0: 'Class', arg1: 'ParameterizedType') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.determineTypeArguments(java.lang.Class<?>,java.lang.reflect.ParameterizedType)"""
        return Map.__wrap(__TypeUtils.determineTypeArguments(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def wrap(arg0: 'Type') -> 'Typed':
        """public static <T> org.apache.commons.lang3.reflect.Typed<T> org.apache.commons.lang3.reflect.TypeUtils.wrap(java.lang.reflect.Type)"""
        return Typed.__wrap(__TypeUtils.wrap(arg0))

    @staticmethod
    @overload
    def isArrayType(arg0: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isArrayType(java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.isArrayType(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

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

    @staticmethod
    @overload
    def genericArrayType(arg0: 'Type') -> 'GenericArrayType':
        """public static java.lang.reflect.GenericArrayType org.apache.commons.lang3.reflect.TypeUtils.genericArrayType(java.lang.reflect.Type)"""
        return GenericArrayType.__wrap(__TypeUtils.genericArrayType(arg0))

    @staticmethod
    @overload
    def getTypeArguments(arg0: 'Type', arg1: 'Class') -> 'Map':
        """public static java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type> org.apache.commons.lang3.reflect.TypeUtils.getTypeArguments(java.lang.reflect.Type,java.lang.Class<?>)"""
        return Map.__wrap(__TypeUtils.getTypeArguments(arg0, arg1))

    @staticmethod
    @overload
    def typesSatisfyVariables(arg0: 'Map') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.typesSatisfyVariables(java.util.Map<java.lang.reflect.TypeVariable<?>, java.lang.reflect.Type>)"""
        return bool.__wrap(__TypeUtils.typesSatisfyVariables(arg0))

    @staticmethod
    @overload
    def containsTypeVariables(arg0: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.containsTypeVariables(java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.containsTypeVariables(arg0))

    @staticmethod
    @overload
    def isAssignable(arg0: 'Type', arg1: 'Type') -> bool:
        """public static boolean org.apache.commons.lang3.reflect.TypeUtils.isAssignable(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return bool.__wrap(__TypeUtils.isAssignable(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

 
 
 
# CLASS: org.apache.commons.lang3.reflect.TypeUtils 
 
 
# CLASS: org.apache.commons.lang3.reflect.Typed
import org.apache.commons.lang3.reflect.Typed as __Typed
__Typed = __Typed
from abc import abstractmethod, ABC
 
class Typed(ABC):
    """org.apache.commons.lang3.reflect.Typed"""
 
    @staticmethod
    def __wrap(java_value: __Typed) -> 'Typed':
        return Typed(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Typed):
        """
        Dynamic initializer for Typed.
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
    def getType(self, ):
        """public abstract java.lang.reflect.Type org.apache.commons.lang3.reflect.Typed.getType()"""
        pass 
 
 
# CLASS: org.apache.commons.lang3.reflect.FieldUtils
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.reflect.FieldUtils as __FieldUtils
__FieldUtils = __FieldUtils
import java.lang.reflect.Field as Field
from builtins import object
from typing import List
import java.util.List as __List
__List = __List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.reflect.Field as __Field
__Field = __Field
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.util.List as List
from builtins import int
 
class FieldUtils():
    """org.apache.commons.lang3.reflect.FieldUtils"""
 
    @staticmethod
    def __wrap(java_value: __FieldUtils) -> 'FieldUtils':
        return FieldUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __FieldUtils):
        """
        Dynamic initializer for FieldUtils.
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

    @staticmethod
    @overload
    def getFieldsWithAnnotation(arg0: 'Class', arg1: 'Class') -> List['Field']:
        """public static java.lang.reflect.Field[] org.apache.commons.lang3.reflect.FieldUtils.getFieldsWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List[Field].__wrap(__FieldUtils.getFieldsWithAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def readField(arg0: 'Field', arg1: object, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.reflect.Field,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readField(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Class', arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeStaticField(arg0, arg1, arg2, __boolean.valueOf(arg3))

    @staticmethod
    @overload
    def readStaticField(arg0: 'Field', arg1: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.reflect.Field,boolean) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readStaticField(arg0, __boolean.valueOf(arg1)))

    @staticmethod
    @overload
    def getAllFieldsList(arg0: 'Class') -> 'List':
        """public static java.util.List<java.lang.reflect.Field> org.apache.commons.lang3.reflect.FieldUtils.getAllFieldsList(java.lang.Class<?>)"""
        return List.__wrap(__FieldUtils.getAllFieldsList(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def readStaticField(arg0: 'Field') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.reflect.Field) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readStaticField(arg0))

    @staticmethod
    @overload
    def readStaticField(arg0: 'Class', arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.Class<?>,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readStaticField(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def getDeclaredField(arg0: 'Class', arg1: str) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getDeclaredField(java.lang.Class<?>,java.lang.String)"""
        return Field.__wrap(__FieldUtils.getDeclaredField(arg0, arg1))

    @staticmethod
    @overload
    def readField(arg0: object, arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.Object,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readField(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def writeDeclaredField(arg0: object, arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredField(java.lang.Object,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeDeclaredField(arg0, arg1, arg2)

    @staticmethod
    @overload
    def writeField(arg0: object, arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.Object,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeField(arg0, arg1, arg2)

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def writeField(arg0: object, arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.Object,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeField(arg0, arg1, arg2, __boolean.valueOf(arg3))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.FieldUtils()"""
        val = __FieldUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Class', arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeStaticField(arg0, arg1, arg2)

    @staticmethod
    @overload
    def writeDeclaredStaticField(arg0: 'Class', arg1: str, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeDeclaredStaticField(arg0, arg1, arg2)

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def readDeclaredStaticField(arg0: 'Class', arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredStaticField(java.lang.Class<?>,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readDeclaredStaticField(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def getField(arg0: 'Class', arg1: str) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getField(java.lang.Class<?>,java.lang.String)"""
        return Field.__wrap(__FieldUtils.getField(arg0, arg1))

    @staticmethod
    @overload
    def readDeclaredField(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredField(java.lang.Object,java.lang.String) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readDeclaredField(arg0, arg1))

    @staticmethod
    @overload
    def readDeclaredStaticField(arg0: 'Class', arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredStaticField(java.lang.Class<?>,java.lang.String) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readDeclaredStaticField(arg0, arg1))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Field', arg1: object, arg2: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.reflect.Field,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeStaticField(arg0, arg1, __boolean.valueOf(arg2))

    @staticmethod
    @overload
    def getFieldsListWithAnnotation(arg0: 'Class', arg1: 'Class') -> 'List':
        """public static java.util.List<java.lang.reflect.Field> org.apache.commons.lang3.reflect.FieldUtils.getFieldsListWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List.__wrap(__FieldUtils.getFieldsListWithAnnotation(arg0, arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.FieldUtils()"""
        val = __FieldUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def removeFinalModifier(arg0: 'Field'):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.removeFinalModifier(java.lang.reflect.Field)"""
        __FieldUtils.removeFinalModifier(arg0)

    @staticmethod
    @overload
    def getAllFields(arg0: 'Class') -> List['Field']:
        """public static java.lang.reflect.Field[] org.apache.commons.lang3.reflect.FieldUtils.getAllFields(java.lang.Class<?>)"""
        return List[Field].__wrap(__FieldUtils.getAllFields(arg0))

    @staticmethod
    @overload
    def readDeclaredField(arg0: object, arg1: str, arg2: bool) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readDeclaredField(java.lang.Object,java.lang.String,boolean) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readDeclaredField(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def writeField(arg0: 'Field', arg1: object, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.reflect.Field,java.lang.Object,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeField(arg0, arg1, arg2, __boolean.valueOf(arg3))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getDeclaredField(arg0: 'Class', arg1: str, arg2: bool) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getDeclaredField(java.lang.Class<?>,java.lang.String,boolean)"""
        return Field.__wrap(__FieldUtils.getDeclaredField(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def writeField(arg0: 'Field', arg1: object, arg2: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeField(java.lang.reflect.Field,java.lang.Object,java.lang.Object) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeField(arg0, arg1, arg2)

    @staticmethod
    @overload
    def readStaticField(arg0: 'Class', arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readStaticField(java.lang.Class<?>,java.lang.String) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readStaticField(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def writeDeclaredStaticField(arg0: 'Class', arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredStaticField(java.lang.Class<?>,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeDeclaredStaticField(arg0, arg1, arg2, __boolean.valueOf(arg3))

    @staticmethod
    @overload
    def readField(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.Object,java.lang.String) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readField(arg0, arg1))

    @staticmethod
    @overload
    def readField(arg0: 'Field', arg1: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.FieldUtils.readField(java.lang.reflect.Field,java.lang.Object) throws java.lang.IllegalAccessException"""
        return object.__wrap(__FieldUtils.readField(arg0, arg1))

    @staticmethod
    @overload
    def writeStaticField(arg0: 'Field', arg1: object):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeStaticField(java.lang.reflect.Field,java.lang.Object) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeStaticField(arg0, arg1)

    @staticmethod
    @overload
    def removeFinalModifier(arg0: 'Field', arg1: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.removeFinalModifier(java.lang.reflect.Field,boolean)"""
        __FieldUtils.removeFinalModifier(arg0, __boolean.valueOf(arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def getField(arg0: 'Class', arg1: str, arg2: bool) -> 'Field':
        """public static java.lang.reflect.Field org.apache.commons.lang3.reflect.FieldUtils.getField(java.lang.Class<?>,java.lang.String,boolean)"""
        return Field.__wrap(__FieldUtils.getField(arg0, arg1, __boolean.valueOf(arg2)))

    @staticmethod
    @overload
    def writeDeclaredField(arg0: object, arg1: str, arg2: object, arg3: bool):
        """public static void org.apache.commons.lang3.reflect.FieldUtils.writeDeclaredField(java.lang.Object,java.lang.String,java.lang.Object,boolean) throws java.lang.IllegalAccessException"""
        __FieldUtils.writeDeclaredField(arg0, arg1, arg2, __boolean.valueOf(arg3)) 
 
 
# CLASS: org.apache.commons.lang3.reflect.ConstructorUtils
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
import org.apache.commons.lang3.reflect.ConstructorUtils as __ConstructorUtils
__ConstructorUtils = __ConstructorUtils
import java.lang.reflect.Constructor as __Constructor
__Constructor = __Constructor
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import java.lang.reflect.Constructor as Constructor
from builtins import int
 
class ConstructorUtils():
    """org.apache.commons.lang3.reflect.ConstructorUtils"""
 
    @staticmethod
    def __wrap(java_value: __ConstructorUtils) -> 'ConstructorUtils':
        return ConstructorUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ConstructorUtils):
        """
        Dynamic initializer for ConstructorUtils.
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

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def invokeConstructor(arg0: 'Class', arg1: 'Object', arg2: 'Class') -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeConstructor(java.lang.Class<T>,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object.__wrap(__ConstructorUtils.invokeConstructor(arg0, arg1, arg2))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.ConstructorUtils()"""
        val = __ConstructorUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def invokeExactConstructor(arg0: 'Class', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeExactConstructor(java.lang.Class<T>,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object.__wrap(__ConstructorUtils.invokeExactConstructor(arg0, arg1))

    @staticmethod
    @overload
    def invokeExactConstructor(arg0: 'Class', arg1: 'Object', arg2: 'Class') -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeExactConstructor(java.lang.Class<T>,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object.__wrap(__ConstructorUtils.invokeExactConstructor(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokeConstructor(arg0: 'Class', *arg1: object) -> object:
        """public static <T> T org.apache.commons.lang3.reflect.ConstructorUtils.invokeConstructor(java.lang.Class<T>,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException,java.lang.InstantiationException"""
        return object.__wrap(__ConstructorUtils.invokeConstructor(arg0, arg1))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getMatchingAccessibleConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getMatchingAccessibleConstructor(java.lang.Class<T>,java.lang.Class<?>...)"""
        return Constructor.__wrap(__ConstructorUtils.getMatchingAccessibleConstructor(arg0, arg1))

    @staticmethod
    @overload
    def getAccessibleConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getAccessibleConstructor(java.lang.Class<T>,java.lang.Class<?>...)"""
        return Constructor.__wrap(__ConstructorUtils.getAccessibleConstructor(arg0, arg1))

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

    @staticmethod
    @overload
    def getAccessibleConstructor(arg0: 'Constructor') -> 'Constructor':
        """public static <T> java.lang.reflect.Constructor<T> org.apache.commons.lang3.reflect.ConstructorUtils.getAccessibleConstructor(java.lang.reflect.Constructor<T>)"""
        return Constructor.__wrap(__ConstructorUtils.getAccessibleConstructor(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.ConstructorUtils()"""
        val = __ConstructorUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.reflect.MethodUtils
from pyquantum_helper import import_once as __import_once__
import org.apache.commons.lang3.reflect.MethodUtils as __MethodUtils
__MethodUtils = __MethodUtils
import java.lang.Boolean as __boolean
from builtins import type
import java.lang.annotation.Annotation as Annotation
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
from builtins import bool
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
import java.util.Set as __Set
__Set = __Set
from builtins import object
from typing import List
import java.util.Set as Set
import java.util.List as __List
__List = __List
import java.lang.Long as __long
try:
    from pyapache import lang3
except ImportError:
    lang3 = __import_once__("pyapache.lang3")

import java.lang.String as __String
__String = __String
import java.lang.reflect.Method as __Method
__Method = __Method
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
import java.lang.reflect.Method as Method
import java.util.List as List
from builtins import int
 
class MethodUtils():
    """org.apache.commons.lang3.reflect.MethodUtils"""
 
    @staticmethod
    def __wrap(java_value: __MethodUtils) -> 'MethodUtils':
        return MethodUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __MethodUtils):
        """
        Dynamic initializer for MethodUtils.
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
    def invokeMethod(arg0: object, arg1: bool, arg2: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,boolean,java.lang.String) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeMethod(arg0, __boolean.valueOf(arg1), arg2))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @staticmethod
    @overload
    def getAccessibleMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getAccessibleMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...)"""
        return Method.__wrap(__MethodUtils.getAccessibleMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getMethodsListWithAnnotation(arg0: 'Class', arg1: 'Class', arg2: bool, arg3: bool) -> 'List':
        """public static java.util.List<java.lang.reflect.Method> org.apache.commons.lang3.reflect.MethodUtils.getMethodsListWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>,boolean,boolean)"""
        return List.__wrap(__MethodUtils.getMethodsListWithAnnotation(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3)))

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: bool, arg2: str, *arg3: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,boolean,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeMethod(arg0, __boolean.valueOf(arg1), arg2, arg3))

    @staticmethod
    @overload
    def invokeStaticMethod(arg0: 'Class', arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeStaticMethod(arg0, arg1, arg2, arg3))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,java.lang.String) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeMethod(arg0, arg1))

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeMethod(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: bool, arg2: str, arg3: 'Object', arg4: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,boolean,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeMethod(arg0, __boolean.valueOf(arg1), arg2, arg3, arg4))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def invokeExactStaticMethod(arg0: 'Class', arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeExactStaticMethod(arg0, arg1, arg2, arg3))

    @staticmethod
    @overload
    def getMethodsWithAnnotation(arg0: 'Class', arg1: 'Class') -> List['Method']:
        """public static java.lang.reflect.Method[] org.apache.commons.lang3.reflect.MethodUtils.getMethodsWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List[Method].__wrap(__MethodUtils.getMethodsWithAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def invokeExactMethod(arg0: object, arg1: str, arg2: 'Object', arg3: 'Class') -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactMethod(java.lang.Object,java.lang.String,java.lang.Object[],java.lang.Class<?>[]) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeExactMethod(arg0, arg1, arg2, arg3))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def invokeExactStaticMethod(arg0: 'Class', arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeExactStaticMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getMethodsListWithAnnotation(arg0: 'Class', arg1: 'Class') -> 'List':
        """public static java.util.List<java.lang.reflect.Method> org.apache.commons.lang3.reflect.MethodUtils.getMethodsListWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return List.__wrap(__MethodUtils.getMethodsListWithAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def getMatchingAccessibleMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getMatchingAccessibleMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...)"""
        return Method.__wrap(__MethodUtils.getMatchingAccessibleMethod(arg0, arg1, arg2))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def invokeMethod(arg0: object, arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeMethod(java.lang.Object,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeMethod(arg0, arg1, arg2))

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.MethodUtils()"""
        val = __MethodUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def invokeExactMethod(arg0: object, arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactMethod(java.lang.Object,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeExactMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def invokeExactMethod(arg0: object, arg1: str) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeExactMethod(java.lang.Object,java.lang.String) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeExactMethod(arg0, arg1))

    @staticmethod
    @overload
    def getOverrideHierarchy(arg0: 'Method', arg1: 'Interfaces') -> 'Set':
        """public static java.util.Set<java.lang.reflect.Method> org.apache.commons.lang3.reflect.MethodUtils.getOverrideHierarchy(java.lang.reflect.Method,org.apache.commons.lang3.ClassUtils$Interfaces)"""
        return Set.__wrap(__MethodUtils.getOverrideHierarchy(arg0, arg1))

    @staticmethod
    @overload
    def getAccessibleMethod(arg0: 'Method') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getAccessibleMethod(java.lang.reflect.Method)"""
        return Method.__wrap(__MethodUtils.getAccessibleMethod(arg0))

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

    @staticmethod
    @overload
    def getMatchingMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static java.lang.reflect.Method org.apache.commons.lang3.reflect.MethodUtils.getMatchingMethod(java.lang.Class<?>,java.lang.String,java.lang.Class<?>...)"""
        return Method.__wrap(__MethodUtils.getMatchingMethod(arg0, arg1, arg2))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def invokeStaticMethod(arg0: 'Class', arg1: str, *arg2: object) -> object:
        """public static java.lang.Object org.apache.commons.lang3.reflect.MethodUtils.invokeStaticMethod(java.lang.Class<?>,java.lang.String,java.lang.Object...) throws java.lang.NoSuchMethodException,java.lang.IllegalAccessException,java.lang.reflect.InvocationTargetException"""
        return object.__wrap(__MethodUtils.invokeStaticMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getAnnotation(arg0: 'Method', arg1: 'Class', arg2: bool, arg3: bool) -> 'Annotation':
        """public static <A extends java.lang.annotation.Annotation> A org.apache.commons.lang3.reflect.MethodUtils.getAnnotation(java.lang.reflect.Method,java.lang.Class<A>,boolean,boolean)"""
        return Annotation.__wrap(__MethodUtils.getAnnotation(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3)))

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.MethodUtils()"""
        val = __MethodUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getMethodsWithAnnotation(arg0: 'Class', arg1: 'Class', arg2: bool, arg3: bool) -> List['Method']:
        """public static java.lang.reflect.Method[] org.apache.commons.lang3.reflect.MethodUtils.getMethodsWithAnnotation(java.lang.Class<?>,java.lang.Class<? extends java.lang.annotation.Annotation>,boolean,boolean)"""
        return List[Method].__wrap(__MethodUtils.getMethodsWithAnnotation(arg0, arg1, __boolean.valueOf(arg2), __boolean.valueOf(arg3))) 
 
 
# CLASS: org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder
from builtins import str
import java.lang.reflect.WildcardType as WildcardType
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import org.apache.commons.lang3.reflect.TypeUtils as __TypeUtils_WildcardTypeBuilder
__WildcardTypeBuilder = __TypeUtils_WildcardTypeBuilder.WildcardTypeBuilder
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
import java.lang.reflect.WildcardType as __WildcardType
__WildcardType = __WildcardType
from builtins import int
 
class WildcardTypeBuilder(lang3.__Builder, builder.Builder):
    """org.apache.commons.lang3.reflect.TypeUtils.WildcardTypeBuilder"""
 
    @staticmethod
    def __wrap(java_value: __WildcardTypeBuilder) -> 'WildcardTypeBuilder':
        return WildcardTypeBuilder(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __WildcardTypeBuilder):
        """
        Dynamic initializer for WildcardTypeBuilder.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def build(self) -> 'WildcardType':
        """public java.lang.reflect.WildcardType org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder.build()"""
        return 'WildcardType'.__wrap(super(WildcardTypeBuilder, self).build())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def withLowerBounds(self, *arg0: 'Type') -> 'WildcardTypeBuilder':
        """public org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder.withLowerBounds(java.lang.reflect.Type...)"""
        return 'WildcardTypeBuilder'.__wrap(super(__WildcardTypeBuilder, self).withLowerBounds(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

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

    @overload
    def withUpperBounds(self, *arg0: 'Type') -> 'WildcardTypeBuilder':
        """public org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder org.apache.commons.lang3.reflect.TypeUtils$WildcardTypeBuilder.withUpperBounds(java.lang.reflect.Type...)"""
        return 'WildcardTypeBuilder'.__wrap(super(__WildcardTypeBuilder, self).withUpperBounds(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.reflect.TypeLiteral
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.reflect.Type as __Type
__Type = __Type
import java.lang.reflect.Type as Type
import org.apache.commons.lang3.reflect.TypeLiteral as __TypeLiteral
__TypeLiteral = __TypeLiteral
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
 
class TypeLiteral(ABC, __Typed, Typed):
    """org.apache.commons.lang3.reflect.TypeLiteral"""
 
    @staticmethod
    def __wrap(java_value: __TypeLiteral) -> 'TypeLiteral':
        return TypeLiteral(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __TypeLiteral):
        """
        Dynamic initializer for TypeLiteral.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def getType(self) -> 'Type':
        """public java.lang.reflect.Type org.apache.commons.lang3.reflect.TypeLiteral.getType()"""
        return 'Type'.__wrap(super(TypeLiteral, self).getType())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, arg0: object) -> bool:
        """public final boolean org.apache.commons.lang3.reflect.TypeLiteral.equals(java.lang.Object)"""
        return bool.__wrap(super(__TypeLiteral, self).equals(arg0))

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
        return str.__wrap(super(TypeLiteral, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int org.apache.commons.lang3.reflect.TypeLiteral.hashCode()"""
        return int.__wrap(super(TypeLiteral, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0)) 
 
 
# CLASS: org.apache.commons.lang3.reflect.InheritanceUtils
from builtins import str
import java.lang.Long as __long
from pyquantum_helper import override
import java.lang.Class as __Class
__Class = __Class
import java.lang.Object as __object
from builtins import type
import java.lang.String as __String
__String = __String
import org.apache.commons.lang3.reflect.InheritanceUtils as __InheritanceUtils
__InheritanceUtils = __InheritanceUtils
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class InheritanceUtils():
    """org.apache.commons.lang3.reflect.InheritanceUtils"""
 
    @staticmethod
    def __wrap(java_value: __InheritanceUtils) -> 'InheritanceUtils':
        return InheritanceUtils(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __InheritanceUtils):
        """
        Dynamic initializer for InheritanceUtils.
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
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def distance(arg0: 'Class', arg1: 'Class') -> int:
        """public static int org.apache.commons.lang3.reflect.InheritanceUtils.distance(java.lang.Class<?>,java.lang.Class<?>)"""
        return int.__wrap(__InheritanceUtils.distance(arg0, arg1))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def __init__(self):
        """public org.apache.commons.lang3.reflect.InheritanceUtils()"""
        val = __InheritanceUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public org.apache.commons.lang3.reflect.InheritanceUtils()"""
        val = __InheritanceUtils()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))