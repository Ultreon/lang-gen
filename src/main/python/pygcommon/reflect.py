from __future__ import annotations
from overload import overload


 
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
try:
    from pygcommon import io
except ImportError:
    io = _import_once("pygcommon.io")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import java.net.URL as _URL
_URL = _URL
import java.lang.Integer as _int
import com.google.common.reflect.ClassPath as _ClassPath_ResourceInfo
_ResourceInfo = _ClassPath_ResourceInfo.ResourceInfo
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceInfo():
    """com.google.common.reflect.ClassPath.ResourceInfo"""
 
    @staticmethod
    def _wrap(java_value: _ResourceInfo) -> 'ResourceInfo':
        return ResourceInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceInfo):
        """
        Dynamic initializer for ResourceInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.toString()"""
        return str._wrap(super(ResourceInfo, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.ClassPath$ResourceInfo.hashCode()"""
        return int._wrap(super(ResourceInfo, self).hashCode())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def asCharSource(self, charset: 'Charset') -> 'io.CharSource':
        """public final com.google.common.io.CharSource com.google.common.reflect.ClassPath$ResourceInfo.asCharSource(java.nio.charset.Charset)"""
        return 'io.CharSource'._wrap(super(_ResourceInfo, self).asCharSource(charset))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def asByteSource(self) -> 'io.ByteSource':
        """public final com.google.common.io.ByteSource com.google.common.reflect.ClassPath$ResourceInfo.asByteSource()"""
        return 'io.ByteSource'._wrap(super(ResourceInfo, self).asByteSource())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getResourceName(self) -> str:
        """public final java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.getResourceName()"""
        return str._wrap(super(ResourceInfo, self).getResourceName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.ClassPath$ResourceInfo.equals(java.lang.Object)"""
        return bool._wrap(super(_ResourceInfo, self).equals(obj))

    @overload
    def url(self) -> 'URL':
        """public final java.net.URL com.google.common.reflect.ClassPath$ResourceInfo.url()"""
        return 'URL'._wrap(super(ResourceInfo, self).url())

 
 
 
# CLASS: com.google.common.reflect.ClassPath$ResourceInfo
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
try:
    from pygcommon import io
except ImportError:
    io = _import_once("pygcommon.io")

import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import java.net.URL as _URL
_URL = _URL
import java.lang.Integer as _int
import com.google.common.reflect.ClassPath as _ClassPath_ResourceInfo
_ResourceInfo = _ClassPath_ResourceInfo.ResourceInfo
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ResourceInfo():
    """com.google.common.reflect.ClassPath.ResourceInfo"""
 
    @staticmethod
    def _wrap(java_value: _ResourceInfo) -> 'ResourceInfo':
        return ResourceInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ResourceInfo):
        """
        Dynamic initializer for ResourceInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ResourceInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ResourceInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.toString()"""
        return str._wrap(super(ResourceInfo, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.ClassPath$ResourceInfo.hashCode()"""
        return int._wrap(super(ResourceInfo, self).hashCode())

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
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def asCharSource(self, charset: 'Charset') -> 'io.CharSource':
        """public final com.google.common.io.CharSource com.google.common.reflect.ClassPath$ResourceInfo.asCharSource(java.nio.charset.Charset)"""
        return 'io.CharSource'._wrap(super(_ResourceInfo, self).asCharSource(charset))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def asByteSource(self) -> 'io.ByteSource':
        """public final com.google.common.io.ByteSource com.google.common.reflect.ClassPath$ResourceInfo.asByteSource()"""
        return 'io.ByteSource'._wrap(super(ResourceInfo, self).asByteSource())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getResourceName(self) -> str:
        """public final java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.getResourceName()"""
        return str._wrap(super(ResourceInfo, self).getResourceName())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.ClassPath$ResourceInfo.equals(java.lang.Object)"""
        return bool._wrap(super(_ResourceInfo, self).equals(obj))

    @overload
    def url(self) -> 'URL':
        """public final java.net.URL com.google.common.reflect.ClassPath$ResourceInfo.url()"""
        return 'URL'._wrap(super(ResourceInfo, self).url())

 
 
 
# CLASS: com.google.common.reflect.ClassPath$ResourceInfo 
 
 
# CLASS: com.google.common.reflect.Invokable
from pyquantum_helper import import_once as _import_once
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ImmutableList as _ImmutableList
_ImmutableList = _ImmutableList
from abc import abstractmethod, ABC
import java.lang.annotation.Annotation as Annotation
import com.google.common.reflect.TypeToken as _TypeToken
_TypeToken = _TypeToken
import java.util.Set as _Set
_Set = _Set
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Boolean as _boolean
from builtins import bool
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.reflect.Invokable as _Invokable
_Invokable = _Invokable
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.util.Set as Set
import java.lang.Integer as _int
import java.lang.reflect.AnnotatedElement as _AnnotatedElement
_AnnotatedElement = _AnnotatedElement
import java.lang.reflect.Member as _Member
_Member = _Member
import java.lang.Long as _long
from builtins import int
import java.lang.reflect.Method as Method
import java.lang.reflect.Constructor as Constructor
import java.lang.Class as _Class
_Class = _Class
 
class Invokable():
    """com.google.common.reflect.Invokable"""
 
    @staticmethod
    def _wrap(java_value: _Invokable) -> 'Invokable':
        return Invokable(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Invokable):
        """
        Dynamic initializer for Invokable.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Invokable__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Invokable__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def accessFlags(self) -> 'Set':
        """public default java.util.Set<java.lang.reflect.AccessFlag> java.lang.reflect.Member.accessFlags()"""
        return 'Set'._wrap(super(Member, self).accessFlags())

    @overload
    def getAnnotation(self, annotationClass: 'Class') -> 'Annotation':
        """public final <A extends java.lang.annotation.Annotation> A com.google.common.reflect.Invokable.getAnnotation(java.lang.Class<A>)"""
        return 'Annotation'._wrap(super(_Invokable, self).getAnnotation(annotationClass))

    @override
    @overload
    def getName(self) -> str:
        """public final java.lang.String com.google.common.reflect.Invokable.getName()"""
        return str._wrap(super(Invokable, self).getName())

    @override
    @overload
    def getAnnotations(self) -> List['Annotation']:
        """public final java.lang.annotation.Annotation[] com.google.common.reflect.Invokable.getAnnotations()"""
        return List['Annotation']._wrap(super(Invokable, self).getAnnotations())

    @overload
    def isAccessible(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isAccessible()"""
        return bool._wrap(super(Invokable, self).isAccessible())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.Invokable.hashCode()"""
        return int._wrap(super(Invokable, self).hashCode())

    @overload
    def isAbstract(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isAbstract()"""
        return bool._wrap(super(Invokable, self).isAbstract())

    @overload
    def setAccessible(self, flag: bool):
        """public final void com.google.common.reflect.Invokable.setAccessible(boolean)"""
        super(_Invokable, self).setAccessible(_boolean.valueOf(flag))

    @overload
    def getAnnotationsByType(self, arg0: 'Class') -> List['Annotation']:
        """public default <T extends java.lang.annotation.Annotation> T[] java.lang.reflect.AnnotatedElement.getAnnotationsByType(java.lang.Class<T>)"""
        return List['Annotation']._wrap(super(_AnnotatedElement, self).getAnnotationsByType(arg0))

    @overload
    def getExceptionTypes(self) -> 'pygcollect.ImmutableList':
        """public final com.google.common.collect.ImmutableList<com.google.common.reflect.TypeToken<? extends java.lang.Throwable>> com.google.common.reflect.Invokable.getExceptionTypes()"""
        return 'pygcollect.ImmutableList'._wrap(super(Invokable, self).getExceptionTypes())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isAnnotationPresent(self, annotationClass: 'Class') -> bool:
        """public final boolean com.google.common.reflect.Invokable.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool._wrap(super(_Invokable, self).isAnnotationPresent(annotationClass))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isNative(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isNative()"""
        return bool._wrap(super(Invokable, self).isNative())

    @overload
    def returning(self, returnType: 'Class') -> 'Invokable':
        """public final <R1 extends R> com.google.common.reflect.Invokable<T, R1> com.google.common.reflect.Invokable.returning(java.lang.Class<R1>)"""
        return 'Invokable'._wrap(super(_Invokable, self).returning(returnType))

    @abstractmethod
    def getAnnotatedReturnType(self, ):
        """public abstract java.lang.reflect.AnnotatedType com.google.common.reflect.Invokable.getAnnotatedReturnType()"""
        pass

    @overload
    def getDeclaredAnnotationsByType(self, arg0: 'Class') -> List['Annotation']:
        """public default <T extends java.lang.annotation.Annotation> T[] java.lang.reflect.AnnotatedElement.getDeclaredAnnotationsByType(java.lang.Class<T>)"""
        return List['Annotation']._wrap(super(_AnnotatedElement, self).getDeclaredAnnotationsByType(arg0))

    @overload
    def getOwnerType(self) -> 'TypeToken':
        """public com.google.common.reflect.TypeToken<T> com.google.common.reflect.Invokable.getOwnerType()"""
        return 'TypeToken'._wrap(super(Invokable, self).getOwnerType())

    @overload
    def isSynchronized(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isSynchronized()"""
        return bool._wrap(super(Invokable, self).isSynchronized())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.Invokable.toString()"""
        return str._wrap(super(Invokable, self).toString())

    @overload
    def getParameters(self) -> 'pygcollect.ImmutableList':
        """public final com.google.common.collect.ImmutableList<com.google.common.reflect.Parameter> com.google.common.reflect.Invokable.getParameters()"""
        return 'pygcollect.ImmutableList'._wrap(super(Invokable, self).getParameters())

    @override
    @overload
    def isSynthetic(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isSynthetic()"""
        return bool._wrap(super(Invokable, self).isSynthetic())

    @overload
    def isProtected(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isProtected()"""
        return bool._wrap(super(Invokable, self).isProtected())

    @overload
    def isPackagePrivate(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isPackagePrivate()"""
        return bool._wrap(super(Invokable, self).isPackagePrivate())

    @override
    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.common.reflect.Invokable.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Invokable, self).getDeclaringClass())

    @staticmethod
    @overload
    def from(method: 'Method') -> 'Invokable':
        """public static com.google.common.reflect.Invokable<?, java.lang.Object> com.google.common.reflect.Invokable.from(java.lang.reflect.Method)"""
        return Invokable._wrap(_Invokable.from(method))

    @overload
    def trySetAccessible(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.trySetAccessible()"""
        return bool._wrap(super(Invokable, self).trySetAccessible())

    @abstractmethod
    def isVarArgs(self, ):
        """public abstract boolean com.google.common.reflect.Invokable.isVarArgs()"""
        pass

    @override
    @overload
    def getModifiers(self) -> int:
        """public final int com.google.common.reflect.Invokable.getModifiers()"""
        return int._wrap(super(Invokable, self).getModifiers())

    @override
    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public final java.lang.annotation.Annotation[] com.google.common.reflect.Invokable.getDeclaredAnnotations()"""
        return List['Annotation']._wrap(super(Invokable, self).getDeclaredAnnotations())

    @overload
    def isPublic(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isPublic()"""
        return bool._wrap(super(Invokable, self).isPublic())

    @abstractmethod
    def getTypeParameters(self, ):
        """public abstract java.lang.reflect.TypeVariable<?>[] com.google.common.reflect.Invokable.getTypeParameters()"""
        pass

    @overload
    def isStatic(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isStatic()"""
        return bool._wrap(super(Invokable, self).isStatic())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def getDeclaredAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public default <T extends java.lang.annotation.Annotation> T java.lang.reflect.AnnotatedElement.getDeclaredAnnotation(java.lang.Class<T>)"""
        return 'Annotation'._wrap(super(_AnnotatedElement, self).getDeclaredAnnotation(arg0))

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.Invokable.equals(java.lang.Object)"""
        return bool._wrap(super(_Invokable, self).equals(obj))

    @overload
    def returning(self, returnType: 'TypeToken') -> 'Invokable':
        """public final <R1 extends R> com.google.common.reflect.Invokable<T, R1> com.google.common.reflect.Invokable.returning(com.google.common.reflect.TypeToken<R1>)"""
        return 'Invokable'._wrap(super(_Invokable, self).returning(returnType))

    @staticmethod
    @overload
    def from(constructor: 'Constructor') -> 'Invokable':
        """public static <T> com.google.common.reflect.Invokable<T, T> com.google.common.reflect.Invokable.from(java.lang.reflect.Constructor<T>)"""
        return Invokable._wrap(_Invokable.from(constructor))

    @abstractmethod
    def isOverridable(self, ):
        """public abstract boolean com.google.common.reflect.Invokable.isOverridable()"""
        pass

    @overload
    def isPrivate(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isPrivate()"""
        return bool._wrap(super(Invokable, self).isPrivate())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def getReturnType(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<? extends R> com.google.common.reflect.Invokable.getReturnType()"""
        return 'TypeToken'._wrap(super(Invokable, self).getReturnType())

    @overload
    def invoke(self, receiver: object, *args: object) -> object:
        """public final R com.google.common.reflect.Invokable.invoke(T,java.lang.Object...) throws java.lang.reflect.InvocationTargetException,java.lang.IllegalAccessException"""
        return object._wrap(super(_Invokable, self).invoke(receiver, args))

    @overload
    def isFinal(self) -> bool:
        """public final boolean com.google.common.reflect.Invokable.isFinal()"""
        return bool._wrap(super(Invokable, self).isFinal()) 
 
 
# CLASS: com.google.common.reflect.Parameter
from builtins import str
from pyquantum_helper import override
import com.google.common.reflect.Parameter as _Parameter
_Parameter = _Parameter
import java.lang.reflect.AnnotatedType as _AnnotatedType
_AnnotatedType = _AnnotatedType
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.reflect.Invokable as _Invokable
_Invokable = _Invokable
import java.lang.String as _String
_String = _String
import java.lang.annotation.Annotation as Annotation
import com.google.common.reflect.TypeToken as _TypeToken
_TypeToken = _TypeToken
from typing import List
import java.lang.reflect.AnnotatedType as AnnotatedType
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
import java.lang.Class as _Class
_Class = _Class
 
class Parameter():
    """com.google.common.reflect.Parameter"""
 
    @staticmethod
    def _wrap(java_value: _Parameter) -> 'Parameter':
        return Parameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Parameter):
        """
        Dynamic initializer for Parameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Parameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Parameter__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getDeclaringInvokable(self) -> 'Invokable':
        """public com.google.common.reflect.Invokable<?, ?> com.google.common.reflect.Parameter.getDeclaringInvokable()"""
        return 'Invokable'._wrap(super(Parameter, self).getDeclaringInvokable())

    @overload
    def getAnnotation(self, annotationType: 'Class') -> 'Annotation':
        """public <A extends java.lang.annotation.Annotation> A com.google.common.reflect.Parameter.getAnnotation(java.lang.Class<A>)"""
        return 'Annotation'._wrap(super(_Parameter, self).getAnnotation(annotationType))

    @overload
    def getAnnotatedType(self) -> 'AnnotatedType':
        """public java.lang.reflect.AnnotatedType com.google.common.reflect.Parameter.getAnnotatedType()"""
        return 'AnnotatedType'._wrap(super(Parameter, self).getAnnotatedType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.Parameter.toString()"""
        return str._wrap(super(Parameter, self).toString())

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.Parameter.hashCode()"""
        return int._wrap(super(Parameter, self).hashCode())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getDeclaredAnnotation(self, annotationType: 'Class') -> 'Annotation':
        """public <A extends java.lang.annotation.Annotation> A com.google.common.reflect.Parameter.getDeclaredAnnotation(java.lang.Class<A>)"""
        return 'Annotation'._wrap(super(_Parameter, self).getDeclaredAnnotation(annotationType))

    @overload
    def getDeclaredAnnotationsByType(self, annotationType: 'Class') -> List['Annotation']:
        """public <A extends java.lang.annotation.Annotation> A[] com.google.common.reflect.Parameter.getDeclaredAnnotationsByType(java.lang.Class<A>)"""
        return List['Annotation']._wrap(super(_Parameter, self).getDeclaredAnnotationsByType(annotationType))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.Parameter.equals(java.lang.Object)"""
        return bool._wrap(super(_Parameter, self).equals(obj))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public java.lang.annotation.Annotation[] com.google.common.reflect.Parameter.getDeclaredAnnotations()"""
        return List['Annotation']._wrap(super(Parameter, self).getDeclaredAnnotations())

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
    def isAnnotationPresent(self, annotationType: 'Class') -> bool:
        """public boolean com.google.common.reflect.Parameter.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool._wrap(super(_Parameter, self).isAnnotationPresent(annotationType))

    @overload
    def getAnnotationsByType(self, annotationType: 'Class') -> List['Annotation']:
        """public <A extends java.lang.annotation.Annotation> A[] com.google.common.reflect.Parameter.getAnnotationsByType(java.lang.Class<A>)"""
        return List['Annotation']._wrap(super(_Parameter, self).getAnnotationsByType(annotationType))

    @override
    @overload
    def getAnnotations(self) -> List['Annotation']:
        """public java.lang.annotation.Annotation[] com.google.common.reflect.Parameter.getAnnotations()"""
        return List['Annotation']._wrap(super(Parameter, self).getAnnotations())

    @overload
    def getType(self) -> 'TypeToken':
        """public com.google.common.reflect.TypeToken<?> com.google.common.reflect.Parameter.getType()"""
        return 'TypeToken'._wrap(super(Parameter, self).getType()) 
 
 
# CLASS: com.google.common.reflect.MutableTypeToInstanceMap
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import java.util.Set as _Set
_Set = _Set
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import com.google.common.collect.ForwardingMap as _ForwardingMap
_ForwardingMap = _ForwardingMap
import com.google.common.reflect.MutableTypeToInstanceMap as _MutableTypeToInstanceMap
_MutableTypeToInstanceMap = _MutableTypeToInstanceMap
import java.util.function.Function as Function
import java.util.Map as Map
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class MutableTypeToInstanceMap():
    """com.google.common.reflect.MutableTypeToInstanceMap"""
 
    @staticmethod
    def _wrap(java_value: _MutableTypeToInstanceMap) -> 'MutableTypeToInstanceMap':
        return MutableTypeToInstanceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _MutableTypeToInstanceMap):
        """
        Dynamic initializer for MutableTypeToInstanceMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_MutableTypeToInstanceMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_MutableTypeToInstanceMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def remove(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.remove(java.lang.Object)"""
        return object._wrap(super(_pygcollect.ForwardingMap, self).remove(key))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> com.google.common.collect.ForwardingMap.values()"""
        return 'Collection'._wrap(super(pygcollect.ForwardingMap, self).values())

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingMap.clear()"""
        super(pygcollect.ForwardingMap, self).clear()

    @override
    @overload
    def putAll(self, map: 'Map'):
        """public void com.google.common.reflect.MutableTypeToInstanceMap.putAll(java.util.Map<? extends com.google.common.reflect.TypeToken<? extends B>, ? extends B>)"""
        super(_MutableTypeToInstanceMap, self).putAll(map)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<com.google.common.reflect.TypeToken<? extends B>, B>> com.google.common.reflect.MutableTypeToInstanceMap.entrySet()"""
        return 'Set'._wrap(super(MutableTypeToInstanceMap, self).entrySet())

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.equals(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingMap, self).equals(object))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getInstance(self, type: 'Class') -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.getInstance(java.lang.Class<T>)"""
        return object._wrap(super(_MutableTypeToInstanceMap, self).getInstance(type))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def get(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.get(java.lang.Object)"""
        return object._wrap(super(_pygcollect.ForwardingMap, self).get(key))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.collect.ForwardingMap.hashCode()"""
        return int._wrap(super(pygcollect.ForwardingMap, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def containsValue(self, value: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingMap, self).containsValue(value))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @overload
    def putInstance(self, type: 'Class', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.putInstance(java.lang.Class<T>,T)"""
        return object._wrap(super(_MutableTypeToInstanceMap, self).putInstance(type, value))

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @overload
    def __init__(self):
        """public com.google.common.reflect.MutableTypeToInstanceMap()"""
        val = _MutableTypeToInstanceMap()
        self.__wrapper = val

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> com.google.common.collect.ForwardingMap.keySet()"""
        return 'Set'._wrap(super(pygcollect.ForwardingMap, self).keySet())

    @overload
    def containsKey(self, key: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingMap, self).containsKey(key))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def __init__(self, ):
        """public com.google.common.reflect.MutableTypeToInstanceMap()"""
        val = _MutableTypeToInstanceMap()
        self.__wrapper = val

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @overload
    def getInstance(self, type: 'TypeToken') -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.getInstance(com.google.common.reflect.TypeToken<T>)"""
        return object._wrap(super(_MutableTypeToInstanceMap, self).getInstance(type))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def putInstance(self, type: 'TypeToken', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.MutableTypeToInstanceMap.putInstance(com.google.common.reflect.TypeToken<T>,T)"""
        return object._wrap(super(_MutableTypeToInstanceMap, self).putInstance(type, value))

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.isEmpty()"""
        return bool._wrap(super(pygcollect.ForwardingMap, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def put(self, key: 'TypeToken', value: object) -> object:
        """public B com.google.common.reflect.MutableTypeToInstanceMap.put(com.google.common.reflect.TypeToken<? extends B>,B)"""
        return object._wrap(super(_MutableTypeToInstanceMap, self).put(key, value))

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingMap.size()"""
        return int._wrap(super(pygcollect.ForwardingMap, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: com.google.common.reflect.Reflection
import java.lang.reflect.InvocationHandler as InvocationHandler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
from builtins import object
import java.lang.String as _string
import java.lang.Integer as _int
import com.google.common.reflect.Reflection as _Reflection
_Reflection = _Reflection
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Reflection():
    """com.google.common.reflect.Reflection"""
 
    @staticmethod
    def _wrap(java_value: _Reflection) -> 'Reflection':
        return Reflection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Reflection):
        """
        Dynamic initializer for Reflection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Reflection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Reflection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def getPackageName(classFullName: str) -> str:
        """public static java.lang.String com.google.common.reflect.Reflection.getPackageName(java.lang.String)"""
        return str._wrap(_Reflection.getPackageName(classFullName))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getPackageName(clazz: 'Class') -> str:
        """public static java.lang.String com.google.common.reflect.Reflection.getPackageName(java.lang.Class<?>)"""
        return str._wrap(_Reflection.getPackageName(clazz))

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

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def initialize(*classes: 'type.Class'):
        """public static void com.google.common.reflect.Reflection.initialize(java.lang.Class<?>...)"""
        _Reflection.initialize(classes)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def newProxy(interfaceType: 'Class', handler: 'InvocationHandler') -> object:
        """public static <T> T com.google.common.reflect.Reflection.newProxy(java.lang.Class<T>,java.lang.reflect.InvocationHandler)"""
        return object._wrap(_Reflection.newProxy(interfaceType, handler))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.reflect.TypeToken
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.reflect.Invokable as _Invokable
_Invokable = _Invokable
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.reflect.Type as _Type
_Type = _Type
import com.google.common.reflect.TypeToken as _TypeToken
_TypeToken = _TypeToken
import java.lang.Integer as _int
import com.google.common.reflect.TypeToken as _TypeToken_TypeSet
_TypeSet = _TypeToken_TypeSet.TypeSet
from builtins import bool
import java.lang.Long as _long
import java.lang.reflect.Method as Method
from builtins import int
import java.lang.reflect.Constructor as Constructor
import java.lang.Class as _Class
_Class = _Class
 
class TypeToken():
    """com.google.common.reflect.TypeToken"""
 
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
    def unwrap(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.unwrap()"""
        return 'TypeToken'._wrap(super(TypeToken, self).unwrap())

    @overload
    def getSubtype(self, subclass: 'Class') -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<? extends T> com.google.common.reflect.TypeToken.getSubtype(java.lang.Class<?>)"""
        return 'TypeToken'._wrap(super(_TypeToken, self).getSubtype(subclass))

    @staticmethod
    @overload
    def of(type: 'Class') -> 'TypeToken':
        """public static <T> com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.of(java.lang.Class<T>)"""
        return TypeToken._wrap(_TypeToken.of(type))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.TypeToken.toString()"""
        return str._wrap(super(TypeToken, self).toString())

    @overload
    def isPrimitive(self) -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isPrimitive()"""
        return bool._wrap(super(TypeToken, self).isPrimitive())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getSupertype(self, superclass: 'Class') -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<? super T> com.google.common.reflect.TypeToken.getSupertype(java.lang.Class<? super T>)"""
        return 'TypeToken'._wrap(super(_TypeToken, self).getSupertype(superclass))

    @overload
    def method(self, method: 'Method') -> 'Invokable':
        """public final com.google.common.reflect.Invokable<T, java.lang.Object> com.google.common.reflect.TypeToken.method(java.lang.reflect.Method)"""
        return 'Invokable'._wrap(super(_TypeToken, self).method(method))

    @overload
    def getRawType(self) -> 'type.Class':
        """public final java.lang.Class<? super T> com.google.common.reflect.TypeToken.getRawType()"""
        return 'type.Class'._wrap(super(TypeToken, self).getRawType())

    @overload
    def isArray(self) -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isArray()"""
        return bool._wrap(super(TypeToken, self).isArray())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def of(type: 'Type') -> 'TypeToken':
        """public static com.google.common.reflect.TypeToken<?> com.google.common.reflect.TypeToken.of(java.lang.reflect.Type)"""
        return TypeToken._wrap(_TypeToken.of(type))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getComponentType(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<?> com.google.common.reflect.TypeToken.getComponentType()"""
        return 'TypeToken'._wrap(super(TypeToken, self).getComponentType())

    @overload
    def where(self, typeParam: 'TypeParameter', typeArg: 'Class') -> 'TypeToken':
        """public final <X> com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.where(com.google.common.reflect.TypeParameter<X>,java.lang.Class<X>)"""
        return 'TypeToken'._wrap(super(_TypeToken, self).where(typeParam, typeArg))

    @overload
    def isSubtypeOf(self, supertype: 'Type') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSubtypeOf(java.lang.reflect.Type)"""
        return bool._wrap(super(_TypeToken, self).isSubtypeOf(supertype))

    @overload
    def resolveType(self, type: 'Type') -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<?> com.google.common.reflect.TypeToken.resolveType(java.lang.reflect.Type)"""
        return 'TypeToken'._wrap(super(_TypeToken, self).resolveType(type))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.TypeToken.hashCode()"""
        return int._wrap(super(TypeToken, self).hashCode())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def where(self, typeParam: 'TypeParameter', typeArg: 'TypeToken') -> 'TypeToken':
        """public final <X> com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.where(com.google.common.reflect.TypeParameter<X>,com.google.common.reflect.TypeToken<X>)"""
        return 'TypeToken'._wrap(super(_TypeToken, self).where(typeParam, typeArg))

    @overload
    def getTypes(self) -> 'TypeSet':
        """public final com.google.common.reflect.TypeToken<T>$TypeSet com.google.common.reflect.TypeToken.getTypes()"""
        return 'TypeSet'._wrap(super(TypeToken, self).getTypes())

    @overload
    def equals(self, o: object) -> bool:
        """public boolean com.google.common.reflect.TypeToken.equals(java.lang.Object)"""
        return bool._wrap(super(_TypeToken, self).equals(o))

    @overload
    def isSupertypeOf(self, type: 'Type') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSupertypeOf(java.lang.reflect.Type)"""
        return bool._wrap(super(_TypeToken, self).isSupertypeOf(type))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isSubtypeOf(self, type: 'TypeToken') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSubtypeOf(com.google.common.reflect.TypeToken<?>)"""
        return bool._wrap(super(_TypeToken, self).isSubtypeOf(type))

    @overload
    def wrap(self) -> 'TypeToken':
        """public final com.google.common.reflect.TypeToken<T> com.google.common.reflect.TypeToken.wrap()"""
        return 'TypeToken'._wrap(super(TypeToken, self).wrap())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isSupertypeOf(self, type: 'TypeToken') -> bool:
        """public final boolean com.google.common.reflect.TypeToken.isSupertypeOf(com.google.common.reflect.TypeToken<?>)"""
        return bool._wrap(super(_TypeToken, self).isSupertypeOf(type))

    @overload
    def constructor(self, constructor: 'Constructor') -> 'Invokable':
        """public final com.google.common.reflect.Invokable<T, T> com.google.common.reflect.TypeToken.constructor(java.lang.reflect.Constructor<?>)"""
        return 'Invokable'._wrap(super(_TypeToken, self).constructor(constructor))

    @overload
    def getType(self) -> 'Type':
        """public final java.lang.reflect.Type com.google.common.reflect.TypeToken.getType()"""
        return 'Type'._wrap(super(TypeToken, self).getType()) 
 
 
# CLASS: com.google.common.reflect.ImmutableTypeToInstanceMap
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import java.util.Map as _Map
_Map = _Map
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _object
import com.google.common.reflect.ImmutableTypeToInstanceMap as _ImmutableTypeToInstanceMap_Builder
_Builder = _ImmutableTypeToInstanceMap_Builder.Builder
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.function.BiFunction as BiFunction
import com.google.common.reflect.ImmutableTypeToInstanceMap as _ImmutableTypeToInstanceMap
_ImmutableTypeToInstanceMap = _ImmutableTypeToInstanceMap
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.util.function.BiConsumer as BiConsumer
import com.google.common.collect.ForwardingMap as _ForwardingMap
_ForwardingMap = _ForwardingMap
import java.util.function.Function as Function
import java.util.Map as Map
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ImmutableTypeToInstanceMap():
    """com.google.common.reflect.ImmutableTypeToInstanceMap"""
 
    @staticmethod
    def _wrap(java_value: _ImmutableTypeToInstanceMap) -> 'ImmutableTypeToInstanceMap':
        return ImmutableTypeToInstanceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ImmutableTypeToInstanceMap):
        """
        Dynamic initializer for ImmutableTypeToInstanceMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ImmutableTypeToInstanceMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ImmutableTypeToInstanceMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def of() -> 'ImmutableTypeToInstanceMap':
        """public static <B> com.google.common.reflect.ImmutableTypeToInstanceMap<B> com.google.common.reflect.ImmutableTypeToInstanceMap.of()"""
        return ImmutableTypeToInstanceMap._wrap(_ImmutableTypeToInstanceMap.of())

    @overload
    def remove(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.remove(java.lang.Object)"""
        return object._wrap(super(_pygcollect.ForwardingMap, self).remove(key))

    @override
    @overload
    def values(self) -> 'Collection':
        """public java.util.Collection<V> com.google.common.collect.ForwardingMap.values()"""
        return 'Collection'._wrap(super(pygcollect.ForwardingMap, self).values())

    @overload
    def putInstance(self, type: 'Class', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.putInstance(java.lang.Class<T>,T)"""
        return object._wrap(super(_ImmutableTypeToInstanceMap, self).putInstance(type, value))

    @overload
    def putInstance(self, type: 'TypeToken', value: object) -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.putInstance(com.google.common.reflect.TypeToken<T>,T)"""
        return object._wrap(super(_ImmutableTypeToInstanceMap, self).putInstance(type, value))

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingMap.clear()"""
        super(pygcollect.ForwardingMap, self).clear()

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getInstance(self, type: 'TypeToken') -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.getInstance(com.google.common.reflect.TypeToken<T>)"""
        return object._wrap(super(_ImmutableTypeToInstanceMap, self).getInstance(type))

    @overload
    def getInstance(self, type: 'Class') -> object:
        """public <T extends B> T com.google.common.reflect.ImmutableTypeToInstanceMap.getInstance(java.lang.Class<T>)"""
        return object._wrap(super(_ImmutableTypeToInstanceMap, self).getInstance(type))

    @override
    @overload
    def putAll(self, map: 'Map'):
        """public void com.google.common.reflect.ImmutableTypeToInstanceMap.putAll(java.util.Map<? extends com.google.common.reflect.TypeToken<? extends B>, ? extends B>)"""
        super(_ImmutableTypeToInstanceMap, self).putAll(map)

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.equals(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingMap, self).equals(object))

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
    def get(self, key: object) -> object:
        """public V com.google.common.collect.ForwardingMap.get(java.lang.Object)"""
        return object._wrap(super(_pygcollect.ForwardingMap, self).get(key))

    @overload
    def put(self, key: 'TypeToken', value: object) -> object:
        """public B com.google.common.reflect.ImmutableTypeToInstanceMap.put(com.google.common.reflect.TypeToken<? extends B>,B)"""
        return object._wrap(super(_ImmutableTypeToInstanceMap, self).put(key, value))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.collect.ForwardingMap.hashCode()"""
        return int._wrap(super(pygcollect.ForwardingMap, self).hashCode())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def containsValue(self, value: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsValue(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingMap, self).containsValue(value))

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @override
    @overload
    def entrySet(self) -> 'Set':
        """public java.util.Set<java.util.Map$Entry<K, V>> com.google.common.collect.ForwardingMap.entrySet()"""
        return 'Set'._wrap(super(pygcollect.ForwardingMap, self).entrySet())

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @override
    @overload
    def keySet(self) -> 'Set':
        """public java.util.Set<K> com.google.common.collect.ForwardingMap.keySet()"""
        return 'Set'._wrap(super(pygcollect.ForwardingMap, self).keySet())

    @overload
    def containsKey(self, key: object) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.containsKey(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingMap, self).containsKey(key))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def builder() -> 'Builder':
        """public static <B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder<B> com.google.common.reflect.ImmutableTypeToInstanceMap.builder()"""
        return Builder._wrap(_ImmutableTypeToInstanceMap.builder())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingMap.isEmpty()"""
        return bool._wrap(super(pygcollect.ForwardingMap, self).isEmpty())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingMap.size()"""
        return int._wrap(super(pygcollect.ForwardingMap, self).size())

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: com.google.common.reflect.ImmutableTypeToInstanceMap$Builder
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.google.common.reflect.ImmutableTypeToInstanceMap as _ImmutableTypeToInstanceMap_Builder
_Builder = _ImmutableTypeToInstanceMap_Builder.Builder
import java.lang.String as _String
_String = _String
import com.google.common.reflect.ImmutableTypeToInstanceMap as _ImmutableTypeToInstanceMap
_ImmutableTypeToInstanceMap = _ImmutableTypeToInstanceMap
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class Builder():
    """com.google.common.reflect.ImmutableTypeToInstanceMap.Builder"""
 
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
    def build(self) -> 'ImmutableTypeToInstanceMap':
        """public com.google.common.reflect.ImmutableTypeToInstanceMap<B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder.build()"""
        return 'ImmutableTypeToInstanceMap'._wrap(super(Builder, self).build())

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
    def put(self, key: 'Class', value: object) -> 'Builder':
        """public <T extends B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder<B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder.put(java.lang.Class<T>,T)"""
        return 'Builder'._wrap(super(_Builder, self).put(key, value))

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
    def put(self, key: 'TypeToken', value: object) -> 'Builder':
        """public <T extends B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder<B> com.google.common.reflect.ImmutableTypeToInstanceMap$Builder.put(com.google.common.reflect.TypeToken<T>,T)"""
        return 'Builder'._wrap(super(_Builder, self).put(key, value))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.reflect.ClassPath
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.String as _String
_String = _String
import java.lang.String as _string
try:
    import pygcollect
except ImportError:
    pygcollect = _import_once("pygcollect")

import java.lang.Integer as _int
import com.google.common.reflect.ClassPath as _ClassPath
_ClassPath = _ClassPath
import java.lang.ClassLoader as ClassLoader
import com.google.common.collect.ImmutableSet as _ImmutableSet
_ImmutableSet = _ImmutableSet
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ClassPath():
    """com.google.common.reflect.ClassPath"""
 
    @staticmethod
    def _wrap(java_value: _ClassPath) -> 'ClassPath':
        return ClassPath(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClassPath):
        """
        Dynamic initializer for ClassPath.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClassPath__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClassPath__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def getAllClasses(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getAllClasses()"""
        return 'pygcollect.ImmutableSet'._wrap(super(ClassPath, self).getAllClasses())

    @overload
    def getTopLevelClasses(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClasses()"""
        return 'pygcollect.ImmutableSet'._wrap(super(ClassPath, self).getTopLevelClasses())

    @overload
    def getResources(self) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ResourceInfo> com.google.common.reflect.ClassPath.getResources()"""
        return 'pygcollect.ImmutableSet'._wrap(super(ClassPath, self).getResources())

    @overload
    def getTopLevelClassesRecursive(self, packageName: str) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClassesRecursive(java.lang.String)"""
        return 'pygcollect.ImmutableSet'._wrap(super(_ClassPath, self).getTopLevelClassesRecursive(packageName))

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

    @staticmethod
    @overload
    def from(classloader: 'ClassLoader') -> 'ClassPath':
        """public static com.google.common.reflect.ClassPath com.google.common.reflect.ClassPath.from(java.lang.ClassLoader) throws java.io.IOException"""
        return ClassPath._wrap(_ClassPath.from(classloader))

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

    @overload
    def getTopLevelClasses(self, packageName: str) -> 'pygcollect.ImmutableSet':
        """public com.google.common.collect.ImmutableSet<com.google.common.reflect.ClassPath$ClassInfo> com.google.common.reflect.ClassPath.getTopLevelClasses(java.lang.String)"""
        return 'pygcollect.ImmutableSet'._wrap(super(_ClassPath, self).getTopLevelClasses(packageName))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.google.common.reflect.TypeParameter
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Integer as _int
import java.lang.Object as _object
from builtins import type
import com.google.common.reflect.TypeParameter as _TypeParameter
_TypeParameter = _TypeParameter
import java.lang.String as _String
_String = _String
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TypeParameter():
    """com.google.common.reflect.TypeParameter"""
 
    @staticmethod
    def _wrap(java_value: _TypeParameter) -> 'TypeParameter':
        return TypeParameter(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeParameter):
        """
        Dynamic initializer for TypeParameter.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeParameter__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeParameter__wrapper":
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
    def hashCode(self) -> int:
        """public final int com.google.common.reflect.TypeParameter.hashCode()"""
        return int._wrap(super(TypeParameter, self).hashCode())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def equals(self, o: object) -> bool:
        """public final boolean com.google.common.reflect.TypeParameter.equals(java.lang.Object)"""
        return bool._wrap(super(_TypeParameter, self).equals(o))

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
        """public java.lang.String com.google.common.reflect.TypeParameter.toString()"""
        return str._wrap(super(TypeParameter, self).toString()) 
 
 
# CLASS: com.google.common.reflect.AbstractInvocationHandler
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import java.lang.Integer as _int
import com.google.common.reflect.AbstractInvocationHandler as _AbstractInvocationHandler
_AbstractInvocationHandler = _AbstractInvocationHandler
from builtins import bool
import java.lang.Long as _long
import java.lang.reflect.Method as Method
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class AbstractInvocationHandler():
    """com.google.common.reflect.AbstractInvocationHandler"""
 
    @staticmethod
    def _wrap(java_value: _AbstractInvocationHandler) -> 'AbstractInvocationHandler':
        return AbstractInvocationHandler(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _AbstractInvocationHandler):
        """
        Dynamic initializer for AbstractInvocationHandler.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_AbstractInvocationHandler__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_AbstractInvocationHandler__wrapper":
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
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.AbstractInvocationHandler.toString()"""
        return str._wrap(super(AbstractInvocationHandler, self).toString())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def invoke(self, proxy: object, method: 'Method', args: 'Object') -> object:
        """public final java.lang.Object com.google.common.reflect.AbstractInvocationHandler.invoke(java.lang.Object,java.lang.reflect.Method,java.lang.Object[]) throws java.lang.Throwable"""
        return object._wrap(super(_AbstractInvocationHandler, self).invoke(proxy, method, args))

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
    def __init__(self):
        """public com.google.common.reflect.AbstractInvocationHandler()"""
        val = _AbstractInvocationHandler()
        self.__wrapper = val

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def __init__(self, ):
        """public com.google.common.reflect.AbstractInvocationHandler()"""
        val = _AbstractInvocationHandler()
        self.__wrapper = val

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.AbstractInvocationHandler.equals(java.lang.Object)"""
        return bool._wrap(super(_AbstractInvocationHandler, self).equals(obj))

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.AbstractInvocationHandler.hashCode()"""
        return int._wrap(super(AbstractInvocationHandler, self).hashCode()) 
 
 
# CLASS: com.google.common.reflect.TypeToken$TypeSet
import java.util.function.Predicate as Predicate
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import com.google.common.collect.ForwardingObject as _ForwardingObject
_ForwardingObject = _ForwardingObject
import com.google.common.collect.ForwardingSet as _ForwardingSet
_ForwardingSet = _ForwardingSet
import java.util.Collection as Collection
import java.util.Set as _Set
_Set = _Set
import java.util.function.Consumer as Consumer
import java.util.Spliterator as Spliterator
import com.google.common.collect.ForwardingCollection as _ForwardingCollection
_ForwardingCollection = _ForwardingCollection
import com.google.common.reflect.TypeToken as _TypeToken_TypeSet
_TypeSet = _TypeToken_TypeSet.TypeSet
import java.util.Iterator as _Iterator
_Iterator = _Iterator
from builtins import bool
from builtins import str
from pyquantum_helper import override
import java.util.function.IntFunction as IntFunction
import java.lang.Object as _object
import java.util.Spliterator as _Spliterator
_Spliterator = _Spliterator
from builtins import object
import java.lang.String as _String
_String = _String
import java.util.Iterator as Iterator
from typing import List
import java.util.Set as Set
import java.util.Collection as _Collection
_Collection = _Collection
import java.lang.Integer as _int
import java.lang.Iterable as _Iterable
_Iterable = _Iterable
import java.util.stream.Stream as _Stream
_Stream = _Stream
import java.util.stream.Stream as Stream
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TypeSet():
    """com.google.common.reflect.TypeToken.TypeSet"""
 
    @staticmethod
    def _wrap(java_value: _TypeSet) -> 'TypeSet':
        return TypeSet(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeSet):
        """
        Dynamic initializer for TypeSet.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeSet__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeSet__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def rawTypes(self) -> 'Set':
        """public java.util.Set<java.lang.Class<? super T>> com.google.common.reflect.TypeToken$TypeSet.rawTypes()"""
        return 'Set'._wrap(super(TypeSet, self).rawTypes())

    @overload
    def contains(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.contains(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).contains(object))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def addAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.addAll(java.util.Collection<? extends E>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).addAll(collection))

    @override
    @overload
    def iterator(self) -> 'Iterator':
        """public java.util.Iterator<E> com.google.common.collect.ForwardingCollection.iterator()"""
        return 'Iterator'._wrap(super(pygcollect.ForwardingCollection, self).iterator())

    @override
    @overload
    def parallelStream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.parallelStream()"""
        return 'Stream'._wrap(super(Collection, self).parallelStream())

    @override
    @overload
    def isEmpty(self) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.isEmpty()"""
        return bool._wrap(super(pygcollect.ForwardingCollection, self).isEmpty())

    @overload
    def removeAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.removeAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).removeAll(collection))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def equals(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingSet.equals(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingSet, self).equals(object))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def size(self) -> int:
        """public int com.google.common.collect.ForwardingCollection.size()"""
        return int._wrap(super(pygcollect.ForwardingCollection, self).size())

    @override
    @overload
    def toArray(self) -> List[object]:
        """public java.lang.Object[] com.google.common.collect.ForwardingCollection.toArray()"""
        return List[object]._wrap(super(pygcollect.ForwardingCollection, self).toArray())

    @overload
    def toArray(self, array: 'Object') -> List[object]:
        """public <T> T[] com.google.common.collect.ForwardingCollection.toArray(T[])"""
        return List[object]._wrap(super(_pygcollect.ForwardingCollection, self).toArray(array))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.collect.ForwardingObject.toString()"""
        return str._wrap(super(pygcollect.ForwardingObject, self).toString())

    @overload
    def interfaces(self) -> 'TypeSet':
        """public com.google.common.reflect.TypeToken<T>$TypeSet com.google.common.reflect.TypeToken$TypeSet.interfaces()"""
        return 'TypeSet'._wrap(super(TypeSet, self).interfaces())

    @override
    @overload
    def clear(self):
        """public void com.google.common.collect.ForwardingCollection.clear()"""
        super(pygcollect.ForwardingCollection, self).clear()

    @overload
    def containsAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.containsAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).containsAll(collection))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def retainAll(self, collection: 'Collection') -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.retainAll(java.util.Collection<?>)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).retainAll(collection))

    @overload
    def removeIf(self, arg0: 'Predicate') -> bool:
        """public default boolean java.util.Collection.removeIf(java.util.function.Predicate<? super E>)"""
        return bool._wrap(super(_Collection, self).removeIf(arg0))

    @overload
    def toArray(self, arg0: 'IntFunction') -> List[object]:
        """public default <T> T[] java.util.Collection.toArray(java.util.function.IntFunction<T[]>)"""
        return List[object]._wrap(super(_Collection, self).toArray(arg0))

    @override
    @overload
    def stream(self) -> 'Stream':
        """public default java.util.stream.Stream<E> java.util.Collection.stream()"""
        return 'Stream'._wrap(super(Collection, self).stream())

    @overload
    def remove(self, object: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.remove(java.lang.Object)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).remove(object))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def add(self, element: object) -> bool:
        """public boolean com.google.common.collect.ForwardingCollection.add(E)"""
        return bool._wrap(super(_pygcollect.ForwardingCollection, self).add(element))

    @override
    @overload
    def spliterator(self) -> 'Spliterator':
        """public default java.util.Spliterator<E> java.util.Set.spliterator()"""
        return 'Spliterator'._wrap(super(Set, self).spliterator())

    @overload
    def classes(self) -> 'TypeSet':
        """public com.google.common.reflect.TypeToken<T>$TypeSet com.google.common.reflect.TypeToken$TypeSet.classes()"""
        return 'TypeSet'._wrap(super(TypeSet, self).classes())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.collect.ForwardingSet.hashCode()"""
        return int._wrap(super(pygcollect.ForwardingSet, self).hashCode())

    @override
    @overload
    def forEach(self, arg0: 'Consumer'):
        """public default void java.lang.Iterable.forEach(java.util.function.Consumer<? super T>)"""
        super(_Iterable, self).forEach(arg0) 
 
 
# CLASS: com.google.common.reflect.ClassPath$ClassInfo
from pyquantum_helper import import_once as _import_once
from builtins import str
from pyquantum_helper import override
import java.nio.charset.Charset as Charset
try:
    from pygcommon import io
except ImportError:
    io = _import_once("pygcommon.io")

import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.google.common.io.CharSource as _CharSource
_CharSource = _CharSource
import java.lang.String as _String
_String = _String
import java.net.URL as URL
import com.google.common.io.ByteSource as _ByteSource
_ByteSource = _ByteSource
import com.google.common.reflect.ClassPath as _ClassPath_ClassInfo
_ClassInfo = _ClassPath_ClassInfo.ClassInfo
import java.net.URL as _URL
_URL = _URL
import java.lang.Integer as _int
import com.google.common.reflect.ClassPath as _ClassPath_ResourceInfo
_ResourceInfo = _ClassPath_ResourceInfo.ResourceInfo
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ClassInfo():
    """com.google.common.reflect.ClassPath.ClassInfo"""
 
    @staticmethod
    def _wrap(java_value: _ClassInfo) -> 'ClassInfo':
        return ClassInfo(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClassInfo):
        """
        Dynamic initializer for ClassInfo.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClassInfo__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClassInfo__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def hashCode(self) -> int:
        """public int com.google.common.reflect.ClassPath$ResourceInfo.hashCode()"""
        return int._wrap(super(ResourceInfo, self).hashCode())

    @overload
    def load(self) -> 'type.Class':
        """public java.lang.Class<?> com.google.common.reflect.ClassPath$ClassInfo.load()"""
        return 'type.Class'._wrap(super(ClassInfo, self).load())

    @overload
    def getName(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.getName()"""
        return str._wrap(super(ClassInfo, self).getName())

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
    def isTopLevel(self) -> bool:
        """public boolean com.google.common.reflect.ClassPath$ClassInfo.isTopLevel()"""
        return bool._wrap(super(ClassInfo, self).isTopLevel())

    @overload
    def getSimpleName(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.getSimpleName()"""
        return str._wrap(super(ClassInfo, self).getSimpleName())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def asCharSource(self, charset: 'Charset') -> 'io.CharSource':
        """public final com.google.common.io.CharSource com.google.common.reflect.ClassPath$ResourceInfo.asCharSource(java.nio.charset.Charset)"""
        return 'io.CharSource'._wrap(super(_ResourceInfo, self).asCharSource(charset))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getPackageName(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.getPackageName()"""
        return str._wrap(super(ClassInfo, self).getPackageName())

    @override
    @overload
    def getResourceName(self) -> str:
        """public final java.lang.String com.google.common.reflect.ClassPath$ResourceInfo.getResourceName()"""
        return str._wrap(super(ResourceInfo, self).getResourceName())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def url(self) -> 'URL':
        """public final java.net.URL com.google.common.reflect.ClassPath$ResourceInfo.url()"""
        return 'URL'._wrap(super(ResourceInfo, self).url())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def asByteSource(self) -> 'io.ByteSource':
        """public final com.google.common.io.ByteSource com.google.common.reflect.ClassPath$ResourceInfo.asByteSource()"""
        return 'io.ByteSource'._wrap(super(ResourceInfo, self).asByteSource())

    @overload
    def equals(self, obj: object) -> bool:
        """public boolean com.google.common.reflect.ClassPath$ResourceInfo.equals(java.lang.Object)"""
        return bool._wrap(super(_ResourceInfo, self).equals(obj))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String com.google.common.reflect.ClassPath$ClassInfo.toString()"""
        return str._wrap(super(ClassInfo, self).toString()) 
 
 
# CLASS: com.google.common.reflect.TypeToInstanceMap
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.util.Map as _Map
_Map = _Map
from abc import abstractmethod, ABC
from builtins import object
import java.util.function.BiFunction as BiFunction
import java.util.function.BiConsumer as BiConsumer
import com.google.common.reflect.TypeToInstanceMap as _TypeToInstanceMap
_TypeToInstanceMap = _TypeToInstanceMap
import java.util.function.Function as Function
from builtins import bool
import java.util.Map as Map
 
class TypeToInstanceMap():
    """com.google.common.reflect.TypeToInstanceMap"""
 
    @staticmethod
    def _wrap(java_value: _TypeToInstanceMap) -> 'TypeToInstanceMap':
        return TypeToInstanceMap(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeToInstanceMap):
        """
        Dynamic initializer for TypeToInstanceMap.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeToInstanceMap__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeToInstanceMap__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @abstractmethod
    def getInstance(self, type: 'Class'):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.getInstance(java.lang.Class<T>)"""
        pass

    @abstractmethod
    def isEmpty(self, ):
        """public abstract boolean java.util.Map.isEmpty()"""
        pass

    @abstractmethod
    def putAll(self, arg0: 'Map'):
        """public abstract void java.util.Map.putAll(java.util.Map<? extends K, ? extends V>)"""
        pass

    @abstractmethod
    def put(self, arg0: object, arg1: object):
        """public abstract V java.util.Map.put(K,V)"""
        pass

    @abstractmethod
    def clear(self, ):
        """public abstract void java.util.Map.clear()"""
        pass

    @abstractmethod
    def get(self, arg0: object):
        """public abstract V java.util.Map.get(java.lang.Object)"""
        pass

    @abstractmethod
    def containsValue(self, arg0: object):
        """public abstract boolean java.util.Map.containsValue(java.lang.Object)"""
        pass

    @abstractmethod
    def remove(self, arg0: object):
        """public abstract V java.util.Map.remove(java.lang.Object)"""
        pass

    @abstractmethod
    def getInstance(self, type: 'TypeToken'):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.getInstance(com.google.common.reflect.TypeToken<T>)"""
        pass

    @overload
    def computeIfAbsent(self, arg0: object, arg1: 'Function') -> object:
        """public default V java.util.Map.computeIfAbsent(K,java.util.function.Function<? super K, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfAbsent(arg0, arg1))

    @overload
    def replace(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.replace(K,V)"""
        return object._wrap(super(_Map, self).replace(arg0, arg1))

    @overload
    def compute(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.compute(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).compute(arg0, arg1))

    @abstractmethod
    def putInstance(self, type: 'TypeToken', value: object):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.putInstance(com.google.common.reflect.TypeToken<T>,T)"""
        pass

    @overload
    def replace(self, arg0: object, arg1: object, arg2: object) -> bool:
        """public default boolean java.util.Map.replace(K,V,V)"""
        return bool._wrap(super(_Map, self).replace(arg0, arg1, arg2))

    @override
    @overload
    def replaceAll(self, arg0: 'BiFunction'):
        """public default void java.util.Map.replaceAll(java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        super(_Map, self).replaceAll(arg0)

    @abstractmethod
    def containsKey(self, arg0: object):
        """public abstract boolean java.util.Map.containsKey(java.lang.Object)"""
        pass

    @overload
    def getOrDefault(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.getOrDefault(java.lang.Object,V)"""
        return object._wrap(super(_Map, self).getOrDefault(arg0, arg1))

    @overload
    def putIfAbsent(self, arg0: object, arg1: object) -> object:
        """public default V java.util.Map.putIfAbsent(K,V)"""
        return object._wrap(super(_Map, self).putIfAbsent(arg0, arg1))

    @overload
    def remove(self, arg0: object, arg1: object) -> bool:
        """public default boolean java.util.Map.remove(java.lang.Object,java.lang.Object)"""
        return bool._wrap(super(_Map, self).remove(arg0, arg1))

    @abstractmethod
    def keySet(self, ):
        """public abstract java.util.Set<K> java.util.Map.keySet()"""
        pass

    @abstractmethod
    def hashCode(self, ):
        """public abstract int java.util.Map.hashCode()"""
        pass

    @abstractmethod
    def entrySet(self, ):
        """public abstract java.util.Set<java.util.Map$Entry<K, V>> java.util.Map.entrySet()"""
        pass

    @abstractmethod
    def size(self, ):
        """public abstract int java.util.Map.size()"""
        pass

    @abstractmethod
    def equals(self, arg0: object):
        """public abstract boolean java.util.Map.equals(java.lang.Object)"""
        pass

    @overload
    def merge(self, arg0: object, arg1: object, arg2: 'BiFunction') -> object:
        """public default V java.util.Map.merge(K,V,java.util.function.BiFunction<? super V, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).merge(arg0, arg1, arg2))

    @overload
    def computeIfPresent(self, arg0: object, arg1: 'BiFunction') -> object:
        """public default V java.util.Map.computeIfPresent(K,java.util.function.BiFunction<? super K, ? super V, ? extends V>)"""
        return object._wrap(super(_Map, self).computeIfPresent(arg0, arg1))

    @abstractmethod
    def putInstance(self, type: 'Class', value: object):
        """public abstract <T extends B> T com.google.common.reflect.TypeToInstanceMap.putInstance(java.lang.Class<T>,T)"""
        pass

    @abstractmethod
    def values(self, ):
        """public abstract java.util.Collection<V> java.util.Map.values()"""
        pass

    @override
    @overload
    def forEach(self, arg0: 'BiConsumer'):
        """public default void java.util.Map.forEach(java.util.function.BiConsumer<? super K, ? super V>)"""
        super(_Map, self).forEach(arg0) 
 
 
# CLASS: com.google.common.reflect.TypeResolver
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.lang.reflect.Type as Type
import java.lang.String as _String
_String = _String
import java.lang.reflect.Type as _Type
_Type = _Type
import java.lang.Integer as _int
import com.google.common.reflect.TypeResolver as _TypeResolver
_TypeResolver = _TypeResolver
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class TypeResolver():
    """com.google.common.reflect.TypeResolver"""
 
    @staticmethod
    def _wrap(java_value: _TypeResolver) -> 'TypeResolver':
        return TypeResolver(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _TypeResolver):
        """
        Dynamic initializer for TypeResolver.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_TypeResolver__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_TypeResolver__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def where(self, formal: 'Type', actual: 'Type') -> 'TypeResolver':
        """public com.google.common.reflect.TypeResolver com.google.common.reflect.TypeResolver.where(java.lang.reflect.Type,java.lang.reflect.Type)"""
        return 'TypeResolver'._wrap(super(_TypeResolver, self).where(formal, actual))

    @overload
    def __init__(self, ):
        """public com.google.common.reflect.TypeResolver()"""
        val = _TypeResolver()
        self.__wrapper = val

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

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.google.common.reflect.TypeResolver()"""
        val = _TypeResolver()
        self.__wrapper = val

    @overload
    def resolveType(self, type: 'Type') -> 'Type':
        """public java.lang.reflect.Type com.google.common.reflect.TypeResolver.resolveType(java.lang.reflect.Type)"""
        return 'Type'._wrap(super(_TypeResolver, self).resolveType(type))

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

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())