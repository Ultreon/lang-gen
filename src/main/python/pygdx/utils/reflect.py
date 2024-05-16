from __future__ import annotations
from overload import overload


 
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.reflect.ArrayReflection as _ArrayReflection
_ArrayReflection = _ArrayReflection
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayReflection():
    """com.badlogic.gdx.utils.reflect.ArrayReflection"""
 
    @staticmethod
    def _wrap(java_value: _ArrayReflection) -> 'ArrayReflection':
        return ArrayReflection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayReflection):
        """
        Dynamic initializer for ArrayReflection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayReflection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayReflection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getLength(arg0: object) -> int:
        """public static int com.badlogic.gdx.utils.reflect.ArrayReflection.getLength(java.lang.Object)"""
        return int._wrap(_ArrayReflection.getLength(arg0))

    @staticmethod
    @overload
    def newInstance(arg0: 'Class', arg1: int) -> object:
        """public static java.lang.Object com.badlogic.gdx.utils.reflect.ArrayReflection.newInstance(java.lang.Class,int)"""
        return object._wrap(_ArrayReflection.newInstance(arg0, _int.valueOf(arg1)))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.reflect.ArrayReflection()"""
        val = _ArrayReflection()
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
    def get(arg0: object, arg1: int) -> object:
        """public static java.lang.Object com.badlogic.gdx.utils.reflect.ArrayReflection.get(java.lang.Object,int)"""
        return object._wrap(_ArrayReflection.get(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.reflect.ArrayReflection()"""
        val = _ArrayReflection()
        self.__wrapper = val

    @staticmethod
    @overload
    def set(arg0: object, arg1: int, arg2: object):
        """public static void com.badlogic.gdx.utils.reflect.ArrayReflection.set(java.lang.Object,int,java.lang.Object)"""
        _ArrayReflection.set(arg0, _int.valueOf(arg1), arg2)

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

 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.ArrayReflection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.reflect.ArrayReflection as _ArrayReflection
_ArrayReflection = _ArrayReflection
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ArrayReflection():
    """com.badlogic.gdx.utils.reflect.ArrayReflection"""
 
    @staticmethod
    def _wrap(java_value: _ArrayReflection) -> 'ArrayReflection':
        return ArrayReflection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ArrayReflection):
        """
        Dynamic initializer for ArrayReflection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ArrayReflection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ArrayReflection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def getLength(arg0: object) -> int:
        """public static int com.badlogic.gdx.utils.reflect.ArrayReflection.getLength(java.lang.Object)"""
        return int._wrap(_ArrayReflection.getLength(arg0))

    @staticmethod
    @overload
    def newInstance(arg0: 'Class', arg1: int) -> object:
        """public static java.lang.Object com.badlogic.gdx.utils.reflect.ArrayReflection.newInstance(java.lang.Class,int)"""
        return object._wrap(_ArrayReflection.newInstance(arg0, _int.valueOf(arg1)))

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

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.reflect.ArrayReflection()"""
        val = _ArrayReflection()
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
    def get(arg0: object, arg1: int) -> object:
        """public static java.lang.Object com.badlogic.gdx.utils.reflect.ArrayReflection.get(java.lang.Object,int)"""
        return object._wrap(_ArrayReflection.get(arg0, _int.valueOf(arg1)))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.reflect.ArrayReflection()"""
        val = _ArrayReflection()
        self.__wrapper = val

    @staticmethod
    @overload
    def set(arg0: object, arg1: int, arg2: object):
        """public static void com.badlogic.gdx.utils.reflect.ArrayReflection.set(java.lang.Object,int,java.lang.Object)"""
        _ArrayReflection.set(arg0, _int.valueOf(arg1), arg2)

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

 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.ArrayReflection 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.ReflectionException
from builtins import str
import java.lang.StackTraceElement as _StackTraceElement
_StackTraceElement = _StackTraceElement
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import java.io.PrintWriter as PrintWriter
import java.lang.String as _String
_String = _String
import java.lang.StackTraceElement as StackTraceElement
from typing import List
import java.lang.String as _string
import java.io.PrintStream as PrintStream
import java.lang.Integer as _int
import java.lang.Throwable as _Throwable
_Throwable = _Throwable
import com.badlogic.gdx.utils.reflect.ReflectionException as _ReflectionException
_ReflectionException = _ReflectionException
import java.lang.Throwable as Throwable
from builtins import bool
import java.lang.Long as _long
from builtins import int
import java.lang.Class as _Class
_Class = _Class
 
class ReflectionException():
    """com.badlogic.gdx.utils.reflect.ReflectionException"""
 
    @staticmethod
    def _wrap(java_value: _ReflectionException) -> 'ReflectionException':
        return ReflectionException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ReflectionException):
        """
        Dynamic initializer for ReflectionException.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ReflectionException__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ReflectionException__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str._wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'._wrap(super(Throwable, self).getCause())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.reflect.ReflectionException()"""
        val = _ReflectionException()
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(_Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'._wrap(super(Throwable, self).fillInStackTrace())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable']._wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str._wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(_Throwable, self).printStackTrace(arg0)

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'._wrap(super(_Throwable, self).initCause(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.reflect.ReflectionException()"""
        val = _ReflectionException()
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str._wrap(super(Throwable, self).toString())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.reflect.ReflectionException(java.lang.String)"""
        val = _ReflectionException(arg0)
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.utils.reflect.ReflectionException(java.lang.String,java.lang.Throwable)"""
        val = _ReflectionException(arg0, arg1)
        self.__wrapper = val

    @override
    @overload
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement']._wrap(super(Throwable, self).getStackTrace())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(_Throwable, self).addSuppressed(arg0)

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.utils.reflect.ReflectionException(java.lang.Throwable)"""
        val = _ReflectionException(arg0)
        self.__wrapper = val

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(_Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Method
from builtins import str
import com.badlogic.gdx.utils.reflect.Annotation as _Annotation
_Annotation = _Annotation
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
import com.badlogic.gdx.utils.reflect.Method as _Method
_Method = _Method
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Method():
    """com.badlogic.gdx.utils.reflect.Method"""
 
    @staticmethod
    def _wrap(java_value: _Method) -> 'Method':
        return Method(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Method):
        """
        Dynamic initializer for Method.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Method__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Method__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def invoke(self, arg0: object, *arg1: object) -> object:
        """public java.lang.Object com.badlogic.gdx.utils.reflect.Method.invoke(java.lang.Object,java.lang.Object...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object._wrap(super(_Method, self).invoke(arg0, arg1))

    @overload
    def isStatic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isStatic()"""
        return bool._wrap(super(Method, self).isStatic())

    @overload
    def isVarArgs(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isVarArgs()"""
        return bool._wrap(super(Method, self).isVarArgs())

    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.Method.getDeclaredAnnotations()"""
        return List['Annotation']._wrap(super(Method, self).getDeclaredAnnotations())

    @overload
    def isProtected(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isProtected()"""
        return bool._wrap(super(Method, self).isProtected())

    @overload
    def isAnnotationPresent(self, arg0: 'Class') -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool._wrap(super(_Method, self).isAnnotationPresent(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAccessible(self, arg0: bool):
        """public void com.badlogic.gdx.utils.reflect.Method.setAccessible(boolean)"""
        super(_Method, self).setAccessible(_boolean.valueOf(arg0))

    @overload
    def getReturnType(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Method.getReturnType()"""
        return 'type.Class'._wrap(super(Method, self).getReturnType())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def isDefaultAccess(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isDefaultAccess()"""
        return bool._wrap(super(Method, self).isDefaultAccess())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Method.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Method, self).getDeclaringClass())

    @overload
    def isAccessible(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isAccessible()"""
        return bool._wrap(super(Method, self).isAccessible())

    @overload
    def getParameterTypes(self) -> List['type.Class']:
        """public java.lang.Class[] com.badlogic.gdx.utils.reflect.Method.getParameterTypes()"""
        return List['type.Class']._wrap(super(Method, self).getParameterTypes())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isPrivate(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isPrivate()"""
        return bool._wrap(super(Method, self).isPrivate())

    @overload
    def getDeclaredAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.Method.getDeclaredAnnotation(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return 'Annotation'._wrap(super(_Method, self).getDeclaredAnnotation(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isAbstract(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isAbstract()"""
        return bool._wrap(super(Method, self).isAbstract())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.reflect.Method.getName()"""
        return str._wrap(super(Method, self).getName())

    @overload
    def isFinal(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isFinal()"""
        return bool._wrap(super(Method, self).isFinal())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isNative(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isNative()"""
        return bool._wrap(super(Method, self).isNative())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isPublic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isPublic()"""
        return bool._wrap(super(Method, self).isPublic())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.ClassReflection
from builtins import str
import com.badlogic.gdx.utils.reflect.Constructor as _Constructor
_Constructor = _Constructor
import com.badlogic.gdx.utils.reflect.Annotation as _Annotation
_Annotation = _Annotation
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import com.badlogic.gdx.utils.reflect.Field as _Field
_Field = _Field
from builtins import object
import java.lang.String as _String
_String = _String
import com.badlogic.gdx.utils.reflect.ClassReflection as _ClassReflection
_ClassReflection = _ClassReflection
from typing import List
import java.lang.String as _string
import java.lang.Integer as _int
import com.badlogic.gdx.utils.reflect.Method as _Method
_Method = _Method
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class ClassReflection():
    """com.badlogic.gdx.utils.reflect.ClassReflection"""
 
    @staticmethod
    def _wrap(java_value: _ClassReflection) -> 'ClassReflection':
        return ClassReflection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _ClassReflection):
        """
        Dynamic initializer for ClassReflection.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_ClassReflection__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_ClassReflection__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @staticmethod
    @overload
    def isInstance(arg0: 'Class', arg1: object) -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isInstance(java.lang.Class,java.lang.Object)"""
        return bool._wrap(_ClassReflection.isInstance(arg0, arg1))

    @staticmethod
    @overload
    def getInterfaces(arg0: 'Class') -> List['type.Class']:
        """public static java.lang.Class[] com.badlogic.gdx.utils.reflect.ClassReflection.getInterfaces(java.lang.Class)"""
        return List[type.Class]._wrap(_ClassReflection.getInterfaces(arg0))

    @staticmethod
    @overload
    def isAnnotationPresent(arg0: 'Class', arg1: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAnnotationPresent(java.lang.Class,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool._wrap(_ClassReflection.isAnnotationPresent(arg0, arg1))

    @staticmethod
    @overload
    def getMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static com.badlogic.gdx.utils.reflect.Method com.badlogic.gdx.utils.reflect.ClassReflection.getMethod(java.lang.Class,java.lang.String,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Method._wrap(_ClassReflection.getMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def getDeclaredMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static com.badlogic.gdx.utils.reflect.Method com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredMethod(java.lang.Class,java.lang.String,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Method._wrap(_ClassReflection.getDeclaredMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isInterface(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isInterface(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isInterface(arg0))

    @staticmethod
    @overload
    def getFields(arg0: 'Class') -> List['Field']:
        """public static com.badlogic.gdx.utils.reflect.Field[] com.badlogic.gdx.utils.reflect.ClassReflection.getFields(java.lang.Class)"""
        return List[Field]._wrap(_ClassReflection.getFields(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def newInstance(arg0: 'Class') -> object:
        """public static <T> T com.badlogic.gdx.utils.reflect.ClassReflection.newInstance(java.lang.Class<T>) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object._wrap(_ClassReflection.newInstance(arg0))

    @staticmethod
    @overload
    def getSimpleName(arg0: 'Class') -> str:
        """public static java.lang.String com.badlogic.gdx.utils.reflect.ClassReflection.getSimpleName(java.lang.Class)"""
        return str._wrap(_ClassReflection.getSimpleName(arg0))

    @staticmethod
    @overload
    def isStaticClass(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isStaticClass(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isStaticClass(arg0))

    @staticmethod
    @overload
    def getMethods(arg0: 'Class') -> List['Method']:
        """public static com.badlogic.gdx.utils.reflect.Method[] com.badlogic.gdx.utils.reflect.ClassReflection.getMethods(java.lang.Class)"""
        return List[Method]._wrap(_ClassReflection.getMethods(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @staticmethod
    @overload
    def getEnumConstants(arg0: 'Class') -> List[object]:
        """public static java.lang.Object[] com.badlogic.gdx.utils.reflect.ClassReflection.getEnumConstants(java.lang.Class)"""
        return List[object]._wrap(_ClassReflection.getEnumConstants(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def isAbstract(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAbstract(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isAbstract(arg0))

    @staticmethod
    @overload
    def getComponentType(arg0: 'Class') -> 'type.Class':
        """public static java.lang.Class com.badlogic.gdx.utils.reflect.ClassReflection.getComponentType(java.lang.Class)"""
        return type.Class._wrap(_ClassReflection.getComponentType(arg0))

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.reflect.ClassReflection()"""
        val = _ClassReflection()
        self.__wrapper = val

    @staticmethod
    @overload
    def getConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static com.badlogic.gdx.utils.reflect.Constructor com.badlogic.gdx.utils.reflect.ClassReflection.getConstructor(java.lang.Class,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Constructor._wrap(_ClassReflection.getConstructor(arg0, arg1))

    @staticmethod
    @overload
    def getAnnotation(arg0: 'Class', arg1: 'Class') -> 'Annotation':
        """public static com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.ClassReflection.getAnnotation(java.lang.Class,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return Annotation._wrap(_ClassReflection.getAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def getAnnotations(arg0: 'Class') -> List['Annotation']:
        """public static com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.ClassReflection.getAnnotations(java.lang.Class)"""
        return List[Annotation]._wrap(_ClassReflection.getAnnotations(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @staticmethod
    @overload
    def isAnnotation(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAnnotation(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isAnnotation(arg0))

    @staticmethod
    @overload
    def isArray(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isArray(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isArray(arg0))

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @staticmethod
    @overload
    def isAssignableFrom(arg0: 'Class', arg1: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAssignableFrom(java.lang.Class,java.lang.Class)"""
        return bool._wrap(_ClassReflection.isAssignableFrom(arg0, arg1))

    @staticmethod
    @overload
    def getField(arg0: 'Class', arg1: str) -> 'Field':
        """public static com.badlogic.gdx.utils.reflect.Field com.badlogic.gdx.utils.reflect.ClassReflection.getField(java.lang.Class,java.lang.String) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Field._wrap(_ClassReflection.getField(arg0, arg1))

    @staticmethod
    @overload
    def getDeclaredConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static com.badlogic.gdx.utils.reflect.Constructor com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredConstructor(java.lang.Class,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Constructor._wrap(_ClassReflection.getDeclaredConstructor(arg0, arg1))

    @staticmethod
    @overload
    def getDeclaredAnnotation(arg0: 'Class', arg1: 'Class') -> 'Annotation':
        """public static com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredAnnotation(java.lang.Class,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return Annotation._wrap(_ClassReflection.getDeclaredAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def getConstructors(arg0: 'Class') -> List['Constructor']:
        """public static com.badlogic.gdx.utils.reflect.Constructor[] com.badlogic.gdx.utils.reflect.ClassReflection.getConstructors(java.lang.Class)"""
        return List[Constructor]._wrap(_ClassReflection.getConstructors(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getDeclaredFields(arg0: 'Class') -> List['Field']:
        """public static com.badlogic.gdx.utils.reflect.Field[] com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredFields(java.lang.Class)"""
        return List[Field]._wrap(_ClassReflection.getDeclaredFields(arg0))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.reflect.ClassReflection()"""
        val = _ClassReflection()
        self.__wrapper = val

    @staticmethod
    @overload
    def isPrimitive(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isPrimitive(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isPrimitive(arg0))

    @staticmethod
    @overload
    def getDeclaredMethods(arg0: 'Class') -> List['Method']:
        """public static com.badlogic.gdx.utils.reflect.Method[] com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredMethods(java.lang.Class)"""
        return List[Method]._wrap(_ClassReflection.getDeclaredMethods(arg0))

    @staticmethod
    @overload
    def isMemberClass(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isMemberClass(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isMemberClass(arg0))

    @staticmethod
    @overload
    def forName(arg0: str) -> 'type.Class':
        """public static java.lang.Class com.badlogic.gdx.utils.reflect.ClassReflection.forName(java.lang.String) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return type.Class._wrap(_ClassReflection.forName(arg0))

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
    def isEnum(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isEnum(java.lang.Class)"""
        return bool._wrap(_ClassReflection.isEnum(arg0))

    @staticmethod
    @overload
    def getDeclaredField(arg0: 'Class', arg1: str) -> 'Field':
        """public static com.badlogic.gdx.utils.reflect.Field com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredField(java.lang.Class,java.lang.String) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Field._wrap(_ClassReflection.getDeclaredField(arg0, arg1))

    @staticmethod
    @overload
    def getDeclaredAnnotations(arg0: 'Class') -> List['Annotation']:
        """public static com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredAnnotations(java.lang.Class)"""
        return List[Annotation]._wrap(_ClassReflection.getDeclaredAnnotations(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Annotation
from builtins import str
import com.badlogic.gdx.utils.reflect.Annotation as _Annotation
_Annotation = _Annotation
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
import java.lang.String as _String
_String = _String
import java.lang.annotation.Annotation as Annotation
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.lang.annotation.Annotation as _Annotation
_Annotation = _Annotation
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Annotation():
    """com.badlogic.gdx.utils.reflect.Annotation"""
 
    @staticmethod
    def _wrap(java_value: _Annotation) -> 'Annotation':
        return Annotation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Annotation):
        """
        Dynamic initializer for Annotation.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Annotation__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Annotation__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0))

    @overload
    def getAnnotationType(self) -> 'type.Class':
        """public java.lang.Class<? extends java.lang.annotation.Annotation> com.badlogic.gdx.utils.reflect.Annotation.getAnnotationType()"""
        return 'type.Class'._wrap(super(Annotation, self).getAnnotationType())

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
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public <T extends java.lang.annotation.Annotation> T com.badlogic.gdx.utils.reflect.Annotation.getAnnotation(java.lang.Class<T>)"""
        return 'Annotation'._wrap(super(_Annotation, self).getAnnotation(arg0))

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
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Constructor
import com.badlogic.gdx.utils.reflect.Constructor as _Constructor
_Constructor = _Constructor
from builtins import str
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
from builtins import type
import java.lang.Object as _object
from builtins import object
import java.lang.String as _String
_String = _String
from typing import List
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Constructor():
    """com.badlogic.gdx.utils.reflect.Constructor"""
 
    @staticmethod
    def _wrap(java_value: _Constructor) -> 'Constructor':
        return Constructor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Constructor):
        """
        Dynamic initializer for Constructor.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Constructor__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Constructor__wrapper":
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
    def newInstance(self, *arg0: object) -> object:
        """public java.lang.Object com.badlogic.gdx.utils.reflect.Constructor.newInstance(java.lang.Object...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object._wrap(super(_Constructor, self).newInstance(arg0))

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
    def isAccessible(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Constructor.isAccessible()"""
        return bool._wrap(super(Constructor, self).isAccessible())

    @overload
    def setAccessible(self, arg0: bool):
        """public void com.badlogic.gdx.utils.reflect.Constructor.setAccessible(boolean)"""
        super(_Constructor, self).setAccessible(_boolean.valueOf(arg0))

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
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Constructor.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Constructor, self).getDeclaringClass())

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
    def getParameterTypes(self) -> List['type.Class']:
        """public java.lang.Class[] com.badlogic.gdx.utils.reflect.Constructor.getParameterTypes()"""
        return List['type.Class']._wrap(super(Constructor, self).getParameterTypes())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode()) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Field
from builtins import str
import com.badlogic.gdx.utils.reflect.Annotation as _Annotation
_Annotation = _Annotation
from pyquantum_helper import override
import java.lang.Object as _Object
_Object = _Object
import java.lang.Object as _object
from builtins import type
import com.badlogic.gdx.utils.reflect.Field as _Field
_Field = _Field
import java.lang.String as _String
_String = _String
from builtins import object
from typing import List
import java.lang.Boolean as _boolean
import java.lang.Integer as _int
from builtins import bool
import java.lang.Long as _long
import java.lang.Class as _Class
_Class = _Class
from builtins import int
 
class Field():
    """com.badlogic.gdx.utils.reflect.Field"""
 
    @staticmethod
    def _wrap(java_value: _Field) -> 'Field':
        return Field(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: _Field):
        """
        Dynamic initializer for Field.
        WARNING: DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
 
        :param __dynamic__: The java object to wrap
        """
        self.__wrapper = __dynamic__
 
    def __getattr__(self, name: str):
        print("Getting attribute %s" % name)
        if name == "_Field__wrapper":
            return object.__getattr__(self, name)
        return getattr(self.__wrapper, name)
 
    def __setattr__(self, name: str, value: Any):
        print("Setting attribute %s to %s" % (name, value))
        if name == "_Field__wrapper":
            return object.__setattr__(self, name, value)
        setattr(self.__wrapper, name, value)
 
    def __delattr__(self, name: str):
        raise AttributeError("Cannot delete attribute '%s' from %s" % (name, self.__wrapper.__class__.__name__))
 
    @overload
    def isPrivate(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isPrivate()"""
        return bool._wrap(super(Field, self).isPrivate())

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.reflect.Field.getName()"""
        return str._wrap(super(Field, self).getName())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAccessible(self, arg0: bool):
        """public void com.badlogic.gdx.utils.reflect.Field.setAccessible(boolean)"""
        super(_Field, self).setAccessible(_boolean.valueOf(arg0))

    @overload
    def get(self, arg0: object) -> object:
        """public java.lang.Object com.badlogic.gdx.utils.reflect.Field.get(java.lang.Object) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object._wrap(super(_Field, self).get(arg0))

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Field.getType()"""
        return 'type.Class'._wrap(super(Field, self).getType())

    @overload
    def isProtected(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isProtected()"""
        return bool._wrap(super(Field, self).isProtected())

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
    def isDefaultAccess(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isDefaultAccess()"""
        return bool._wrap(super(Field, self).isDefaultAccess())

    @overload
    def getDeclaredAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.Field.getDeclaredAnnotation(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return 'Annotation'._wrap(super(_Field, self).getDeclaredAnnotation(arg0))

    @overload
    def isTransient(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isTransient()"""
        return bool._wrap(super(Field, self).isTransient())

    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.Field.getDeclaredAnnotations()"""
        return List['Annotation']._wrap(super(Field, self).getDeclaredAnnotations())

    @overload
    def isAccessible(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isAccessible()"""
        return bool._wrap(super(Field, self).isAccessible())

    @overload
    def isSynthetic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isSynthetic()"""
        return bool._wrap(super(Field, self).isSynthetic())

    @overload
    def getElementType(self, arg0: int) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Field.getElementType(int)"""
        return 'type.Class'._wrap(super(_Field, self).getElementType(_int.valueOf(arg0)))

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Field.getDeclaringClass()"""
        return 'type.Class'._wrap(super(Field, self).getDeclaringClass())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool._wrap(super(_object, self).equals(arg0))

    @overload
    def isPublic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isPublic()"""
        return bool._wrap(super(Field, self).isPublic())

    @overload
    def isStatic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isStatic()"""
        return bool._wrap(super(Field, self).isStatic())

    @overload
    def isFinal(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isFinal()"""
        return bool._wrap(super(Field, self).isFinal())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(_object, self).wait(_long.valueOf(arg0), _int.valueOf(arg1))

    @overload
    def isVolatile(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isVolatile()"""
        return bool._wrap(super(Field, self).isVolatile())

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str._wrap(super(object, self).toString())

    @overload
    def set(self, arg0: object, arg1: object):
        """public void com.badlogic.gdx.utils.reflect.Field.set(java.lang.Object,java.lang.Object) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        super(_Field, self).set(arg0, arg1)

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'._wrap(super(object, self).getClass())

    @overload
    def isAnnotationPresent(self, arg0: 'Class') -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool._wrap(super(_Field, self).isAnnotationPresent(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int._wrap(super(object, self).hashCode())