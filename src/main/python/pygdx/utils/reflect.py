from __future__ import annotations
from overload import overload


 
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.annotation.Annotation as Annotation
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.reflect.Annotation as __Annotation
__Annotation = __Annotation
from builtins import int
 
class Annotation():
    """com.badlogic.gdx.utils.reflect.Annotation"""
 
    @staticmethod
    def __wrap(java_value: __Annotation) -> 'Annotation':
        return Annotation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Annotation):
        """
        Dynamic initializer for Annotation.
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

    @overload
    def getAnnotationType(self) -> 'type.Class':
        """public java.lang.Class<? extends java.lang.annotation.Annotation> com.badlogic.gdx.utils.reflect.Annotation.getAnnotationType()"""
        return 'type.Class'.__wrap(super(Annotation, self).getAnnotationType())

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
    def getAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public <T extends java.lang.annotation.Annotation> T com.badlogic.gdx.utils.reflect.Annotation.getAnnotation(java.lang.Class<T>)"""
        return 'Annotation'.__wrap(super(__Annotation, self).getAnnotation(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Annotation
import java.lang.annotation.Annotation as __Annotation
__Annotation = __Annotation
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.annotation.Annotation as Annotation
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.reflect.Annotation as __Annotation
__Annotation = __Annotation
from builtins import int
 
class Annotation():
    """com.badlogic.gdx.utils.reflect.Annotation"""
 
    @staticmethod
    def __wrap(java_value: __Annotation) -> 'Annotation':
        return Annotation(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Annotation):
        """
        Dynamic initializer for Annotation.
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

    @overload
    def getAnnotationType(self) -> 'type.Class':
        """public java.lang.Class<? extends java.lang.annotation.Annotation> com.badlogic.gdx.utils.reflect.Annotation.getAnnotationType()"""
        return 'type.Class'.__wrap(super(Annotation, self).getAnnotationType())

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
    def getAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public <T extends java.lang.annotation.Annotation> T com.badlogic.gdx.utils.reflect.Annotation.getAnnotation(java.lang.Class<T>)"""
        return 'Annotation'.__wrap(super(__Annotation, self).getAnnotation(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Annotation 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.ArrayReflection
import com.badlogic.gdx.utils.reflect.ArrayReflection as __ArrayReflection
__ArrayReflection = __ArrayReflection
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
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
 
class ArrayReflection():
    """com.badlogic.gdx.utils.reflect.ArrayReflection"""
 
    @staticmethod
    def __wrap(java_value: __ArrayReflection) -> 'ArrayReflection':
        return ArrayReflection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ArrayReflection):
        """
        Dynamic initializer for ArrayReflection.
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
    def newInstance(arg0: 'Class', arg1: int) -> object:
        """public static java.lang.Object com.badlogic.gdx.utils.reflect.ArrayReflection.newInstance(java.lang.Class,int)"""
        return object.__wrap(__ArrayReflection.newInstance(arg0, __int.valueOf(arg1)))

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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def get(arg0: object, arg1: int) -> object:
        """public static java.lang.Object com.badlogic.gdx.utils.reflect.ArrayReflection.get(java.lang.Object,int)"""
        return object.__wrap(__ArrayReflection.get(arg0, __int.valueOf(arg1)))

    @staticmethod
    @overload
    def set(arg0: object, arg1: int, arg2: object):
        """public static void com.badlogic.gdx.utils.reflect.ArrayReflection.set(java.lang.Object,int,java.lang.Object)"""
        __ArrayReflection.set(arg0, __int.valueOf(arg1), arg2)

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getLength(arg0: object) -> int:
        """public static int com.badlogic.gdx.utils.reflect.ArrayReflection.getLength(java.lang.Object)"""
        return int.__wrap(__ArrayReflection.getLength(arg0))

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

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.reflect.ArrayReflection()"""
        val = __ArrayReflection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.reflect.ArrayReflection()"""
        val = __ArrayReflection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Field
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import com.badlogic.gdx.utils.reflect.Field as __Field
__Field = __Field
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.reflect.Annotation as __Annotation
__Annotation = __Annotation
from builtins import int
 
class Field():
    """com.badlogic.gdx.utils.reflect.Field"""
 
    @staticmethod
    def __wrap(java_value: __Field) -> 'Field':
        return Field(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Field):
        """
        Dynamic initializer for Field.
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
 
    @overload
    def isPublic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isPublic()"""
        return bool.__wrap(super(Field, self).isPublic())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isAnnotationPresent(self, arg0: 'Class') -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool.__wrap(super(__Field, self).isAnnotationPresent(arg0))

    @overload
    def set(self, arg0: object, arg1: object):
        """public void com.badlogic.gdx.utils.reflect.Field.set(java.lang.Object,java.lang.Object) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        super(__Field, self).set(arg0, arg1)

    @overload
    def isTransient(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isTransient()"""
        return bool.__wrap(super(Field, self).isTransient())

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Field.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Field, self).getDeclaringClass())

    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.Field.getDeclaredAnnotations()"""
        return List['Annotation'].__wrap(super(Field, self).getDeclaredAnnotations())

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.reflect.Field.getName()"""
        return str.__wrap(super(Field, self).getName())

    @overload
    def get(self, arg0: object) -> object:
        """public java.lang.Object com.badlogic.gdx.utils.reflect.Field.get(java.lang.Object) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object.__wrap(super(__Field, self).get(arg0))

    @overload
    def isStatic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isStatic()"""
        return bool.__wrap(super(Field, self).isStatic())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isFinal(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isFinal()"""
        return bool.__wrap(super(Field, self).isFinal())

    @overload
    def getType(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Field.getType()"""
        return 'type.Class'.__wrap(super(Field, self).getType())

    @overload
    def isDefaultAccess(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isDefaultAccess()"""
        return bool.__wrap(super(Field, self).isDefaultAccess())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @overload
    def isProtected(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isProtected()"""
        return bool.__wrap(super(Field, self).isProtected())

    @overload
    def isSynthetic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isSynthetic()"""
        return bool.__wrap(super(Field, self).isSynthetic())

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def isAccessible(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isAccessible()"""
        return bool.__wrap(super(Field, self).isAccessible())

    @overload
    def isPrivate(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isPrivate()"""
        return bool.__wrap(super(Field, self).isPrivate())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def setAccessible(self, arg0: bool):
        """public void com.badlogic.gdx.utils.reflect.Field.setAccessible(boolean)"""
        super(__Field, self).setAccessible(__boolean.valueOf(arg0))

    @overload
    def getElementType(self, arg0: int) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Field.getElementType(int)"""
        return 'type.Class'.__wrap(super(__Field, self).getElementType(__int.valueOf(arg0)))

    @overload
    def getDeclaredAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.Field.getDeclaredAnnotation(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return 'Annotation'.__wrap(super(__Field, self).getDeclaredAnnotation(arg0))

    @overload
    def isVolatile(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Field.isVolatile()"""
        return bool.__wrap(super(Field, self).isVolatile())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait() 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Constructor
import com.badlogic.gdx.utils.reflect.Constructor as __Constructor
__Constructor = __Constructor
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
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
 
class Constructor():
    """com.badlogic.gdx.utils.reflect.Constructor"""
 
    @staticmethod
    def __wrap(java_value: __Constructor) -> 'Constructor':
        return Constructor(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Constructor):
        """
        Dynamic initializer for Constructor.
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

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

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
    def isAccessible(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Constructor.isAccessible()"""
        return bool.__wrap(super(Constructor, self).isAccessible())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def getParameterTypes(self) -> List['type.Class']:
        """public java.lang.Class[] com.badlogic.gdx.utils.reflect.Constructor.getParameterTypes()"""
        return List['type.Class'].__wrap(super(Constructor, self).getParameterTypes())

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Constructor.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Constructor, self).getDeclaringClass())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def setAccessible(self, arg0: bool):
        """public void com.badlogic.gdx.utils.reflect.Constructor.setAccessible(boolean)"""
        super(__Constructor, self).setAccessible(__boolean.valueOf(arg0))

    @overload
    def newInstance(self, *arg0: object) -> object:
        """public java.lang.Object com.badlogic.gdx.utils.reflect.Constructor.newInstance(java.lang.Object...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object.__wrap(super(__Constructor, self).newInstance(arg0))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0)) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.ClassReflection
from builtins import str
import com.badlogic.gdx.utils.reflect.Constructor as __Constructor
__Constructor = __Constructor
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import com.badlogic.gdx.utils.reflect.ClassReflection as __ClassReflection
__ClassReflection = __ClassReflection
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __string
import java.lang.String as __String
__String = __String
import com.badlogic.gdx.utils.reflect.Field as __Field
__Field = __Field
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.reflect.Method as __Method
__Method = __Method
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.reflect.Annotation as __Annotation
__Annotation = __Annotation
from builtins import int
 
class ClassReflection():
    """com.badlogic.gdx.utils.reflect.ClassReflection"""
 
    @staticmethod
    def __wrap(java_value: __ClassReflection) -> 'ClassReflection':
        return ClassReflection(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ClassReflection):
        """
        Dynamic initializer for ClassReflection.
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
    def __init__(self, ):
        """public com.badlogic.gdx.utils.reflect.ClassReflection()"""
        val = __ClassReflection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @staticmethod
    @overload
    def getDeclaredFields(arg0: 'Class') -> List['Field']:
        """public static com.badlogic.gdx.utils.reflect.Field[] com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredFields(java.lang.Class)"""
        return List[Field].__wrap(__ClassReflection.getDeclaredFields(arg0))

    @staticmethod
    @overload
    def newInstance(arg0: 'Class') -> object:
        """public static <T> T com.badlogic.gdx.utils.reflect.ClassReflection.newInstance(java.lang.Class<T>) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object.__wrap(__ClassReflection.newInstance(arg0))

    @staticmethod
    @overload
    def getAnnotation(arg0: 'Class', arg1: 'Class') -> 'Annotation':
        """public static com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.ClassReflection.getAnnotation(java.lang.Class,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return Annotation.__wrap(__ClassReflection.getAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def isAbstract(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAbstract(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isAbstract(arg0))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @staticmethod
    @overload
    def getMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static com.badlogic.gdx.utils.reflect.Method com.badlogic.gdx.utils.reflect.ClassReflection.getMethod(java.lang.Class,java.lang.String,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Method.__wrap(__ClassReflection.getMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isAssignableFrom(arg0: 'Class', arg1: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAssignableFrom(java.lang.Class,java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isAssignableFrom(arg0, arg1))

    @staticmethod
    @overload
    def isEnum(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isEnum(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isEnum(arg0))

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @staticmethod
    @overload
    def getInterfaces(arg0: 'Class') -> List['type.Class']:
        """public static java.lang.Class[] com.badlogic.gdx.utils.reflect.ClassReflection.getInterfaces(java.lang.Class)"""
        return List[type.Class].__wrap(__ClassReflection.getInterfaces(arg0))

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @staticmethod
    @overload
    def getConstructors(arg0: 'Class') -> List['Constructor']:
        """public static com.badlogic.gdx.utils.reflect.Constructor[] com.badlogic.gdx.utils.reflect.ClassReflection.getConstructors(java.lang.Class)"""
        return List[Constructor].__wrap(__ClassReflection.getConstructors(arg0))

    @staticmethod
    @overload
    def getDeclaredAnnotation(arg0: 'Class', arg1: 'Class') -> 'Annotation':
        """public static com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredAnnotation(java.lang.Class,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return Annotation.__wrap(__ClassReflection.getDeclaredAnnotation(arg0, arg1))

    @staticmethod
    @overload
    def getDeclaredAnnotations(arg0: 'Class') -> List['Annotation']:
        """public static com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredAnnotations(java.lang.Class)"""
        return List[Annotation].__wrap(__ClassReflection.getDeclaredAnnotations(arg0))

    @staticmethod
    @overload
    def getAnnotations(arg0: 'Class') -> List['Annotation']:
        """public static com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.ClassReflection.getAnnotations(java.lang.Class)"""
        return List[Annotation].__wrap(__ClassReflection.getAnnotations(arg0))

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @staticmethod
    @overload
    def getMethods(arg0: 'Class') -> List['Method']:
        """public static com.badlogic.gdx.utils.reflect.Method[] com.badlogic.gdx.utils.reflect.ClassReflection.getMethods(java.lang.Class)"""
        return List[Method].__wrap(__ClassReflection.getMethods(arg0))

    @staticmethod
    @overload
    def isStaticClass(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isStaticClass(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isStaticClass(arg0))

    @staticmethod
    @overload
    def isAnnotation(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAnnotation(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isAnnotation(arg0))

    @staticmethod
    @overload
    def getDeclaredField(arg0: 'Class', arg1: str) -> 'Field':
        """public static com.badlogic.gdx.utils.reflect.Field com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredField(java.lang.Class,java.lang.String) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Field.__wrap(__ClassReflection.getDeclaredField(arg0, arg1))

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.reflect.ClassReflection()"""
        val = __ClassReflection()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Object.toString()"""
        return str.__wrap(super(object, self).toString())

    @staticmethod
    @overload
    def getComponentType(arg0: 'Class') -> 'type.Class':
        """public static java.lang.Class com.badlogic.gdx.utils.reflect.ClassReflection.getComponentType(java.lang.Class)"""
        return type.Class.__wrap(__ClassReflection.getComponentType(arg0))

    @staticmethod
    @overload
    def isAnnotationPresent(arg0: 'Class', arg1: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isAnnotationPresent(java.lang.Class,java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool.__wrap(__ClassReflection.isAnnotationPresent(arg0, arg1))

    @staticmethod
    @overload
    def getField(arg0: 'Class', arg1: str) -> 'Field':
        """public static com.badlogic.gdx.utils.reflect.Field com.badlogic.gdx.utils.reflect.ClassReflection.getField(java.lang.Class,java.lang.String) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Field.__wrap(__ClassReflection.getField(arg0, arg1))

    @staticmethod
    @overload
    def isArray(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isArray(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isArray(arg0))

    @staticmethod
    @overload
    def getConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static com.badlogic.gdx.utils.reflect.Constructor com.badlogic.gdx.utils.reflect.ClassReflection.getConstructor(java.lang.Class,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Constructor.__wrap(__ClassReflection.getConstructor(arg0, arg1))

    @staticmethod
    @overload
    def forName(arg0: str) -> 'type.Class':
        """public static java.lang.Class com.badlogic.gdx.utils.reflect.ClassReflection.forName(java.lang.String) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return type.Class.__wrap(__ClassReflection.forName(arg0))

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @staticmethod
    @overload
    def getSimpleName(arg0: 'Class') -> str:
        """public static java.lang.String com.badlogic.gdx.utils.reflect.ClassReflection.getSimpleName(java.lang.Class)"""
        return str.__wrap(__ClassReflection.getSimpleName(arg0))

    @staticmethod
    @overload
    def getFields(arg0: 'Class') -> List['Field']:
        """public static com.badlogic.gdx.utils.reflect.Field[] com.badlogic.gdx.utils.reflect.ClassReflection.getFields(java.lang.Class)"""
        return List[Field].__wrap(__ClassReflection.getFields(arg0))

    @staticmethod
    @overload
    def isInterface(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isInterface(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isInterface(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @staticmethod
    @overload
    def getDeclaredMethod(arg0: 'Class', arg1: str, *arg2: 'type.Class') -> 'Method':
        """public static com.badlogic.gdx.utils.reflect.Method com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredMethod(java.lang.Class,java.lang.String,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Method.__wrap(__ClassReflection.getDeclaredMethod(arg0, arg1, arg2))

    @staticmethod
    @overload
    def isPrimitive(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isPrimitive(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isPrimitive(arg0))

    @staticmethod
    @overload
    def getDeclaredMethods(arg0: 'Class') -> List['Method']:
        """public static com.badlogic.gdx.utils.reflect.Method[] com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredMethods(java.lang.Class)"""
        return List[Method].__wrap(__ClassReflection.getDeclaredMethods(arg0))

    @staticmethod
    @overload
    def getEnumConstants(arg0: 'Class') -> List[object]:
        """public static java.lang.Object[] com.badlogic.gdx.utils.reflect.ClassReflection.getEnumConstants(java.lang.Class)"""
        return List[object].__wrap(__ClassReflection.getEnumConstants(arg0))

    @staticmethod
    @overload
    def isMemberClass(arg0: 'Class') -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isMemberClass(java.lang.Class)"""
        return bool.__wrap(__ClassReflection.isMemberClass(arg0))

    @staticmethod
    @overload
    def getDeclaredConstructor(arg0: 'Class', *arg1: 'type.Class') -> 'Constructor':
        """public static com.badlogic.gdx.utils.reflect.Constructor com.badlogic.gdx.utils.reflect.ClassReflection.getDeclaredConstructor(java.lang.Class,java.lang.Class...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return Constructor.__wrap(__ClassReflection.getDeclaredConstructor(arg0, arg1))

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @staticmethod
    @overload
    def isInstance(arg0: 'Class', arg1: object) -> bool:
        """public static boolean com.badlogic.gdx.utils.reflect.ClassReflection.isInstance(java.lang.Class,java.lang.Object)"""
        return bool.__wrap(__ClassReflection.isInstance(arg0, arg1)) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.Method
from builtins import str
import java.lang.Boolean as __boolean
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
from builtins import object
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.lang.String as __String
__String = __String
import java.lang.Object as __Object
__Object = __Object
import com.badlogic.gdx.utils.reflect.Method as __Method
__Method = __Method
import java.lang.Integer as __int
from builtins import bool
import com.badlogic.gdx.utils.reflect.Annotation as __Annotation
__Annotation = __Annotation
from builtins import int
 
class Method():
    """com.badlogic.gdx.utils.reflect.Method"""
 
    @staticmethod
    def __wrap(java_value: __Method) -> 'Method':
        return Method(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __Method):
        """
        Dynamic initializer for Method.
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
 
    @overload
    def getReturnType(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Method.getReturnType()"""
        return 'type.Class'.__wrap(super(Method, self).getReturnType())

    @override
    @overload
    def wait(self, arg0: int, arg1: int):
        """public final void java.lang.Object.wait(long,int) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0), __int.valueOf(arg1))

    @overload
    def isPublic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isPublic()"""
        return bool.__wrap(super(Method, self).isPublic())

    @overload
    def isAbstract(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isAbstract()"""
        return bool.__wrap(super(Method, self).isAbstract())

    @overload
    def invoke(self, arg0: object, *arg1: object) -> object:
        """public java.lang.Object com.badlogic.gdx.utils.reflect.Method.invoke(java.lang.Object,java.lang.Object...) throws com.badlogic.gdx.utils.reflect.ReflectionException"""
        return object.__wrap(super(__Method, self).invoke(arg0, arg1))

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @overload
    def setAccessible(self, arg0: bool):
        """public void com.badlogic.gdx.utils.reflect.Method.setAccessible(boolean)"""
        super(__Method, self).setAccessible(__boolean.valueOf(arg0))

    @overload
    def getDeclaredAnnotations(self) -> List['Annotation']:
        """public com.badlogic.gdx.utils.reflect.Annotation[] com.badlogic.gdx.utils.reflect.Method.getDeclaredAnnotations()"""
        return List['Annotation'].__wrap(super(Method, self).getDeclaredAnnotations())

    @overload
    def getName(self) -> str:
        """public java.lang.String com.badlogic.gdx.utils.reflect.Method.getName()"""
        return str.__wrap(super(Method, self).getName())

    @overload
    def isAnnotationPresent(self, arg0: 'Class') -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isAnnotationPresent(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return bool.__wrap(super(__Method, self).isAnnotationPresent(arg0))

    @overload
    def isAccessible(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isAccessible()"""
        return bool.__wrap(super(Method, self).isAccessible())

    @overload
    def isPrivate(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isPrivate()"""
        return bool.__wrap(super(Method, self).isPrivate())

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @overload
    def isStatic(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isStatic()"""
        return bool.__wrap(super(Method, self).isStatic())

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def isDefaultAccess(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isDefaultAccess()"""
        return bool.__wrap(super(Method, self).isDefaultAccess())

    @overload
    def isVarArgs(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isVarArgs()"""
        return bool.__wrap(super(Method, self).isVarArgs())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @overload
    def isFinal(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isFinal()"""
        return bool.__wrap(super(Method, self).isFinal())

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

    @overload
    def getDeclaredAnnotation(self, arg0: 'Class') -> 'Annotation':
        """public com.badlogic.gdx.utils.reflect.Annotation com.badlogic.gdx.utils.reflect.Method.getDeclaredAnnotation(java.lang.Class<? extends java.lang.annotation.Annotation>)"""
        return 'Annotation'.__wrap(super(__Method, self).getDeclaredAnnotation(arg0))

    @overload
    def isNative(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isNative()"""
        return bool.__wrap(super(Method, self).isNative())

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @overload
    def getParameterTypes(self) -> List['type.Class']:
        """public java.lang.Class[] com.badlogic.gdx.utils.reflect.Method.getParameterTypes()"""
        return List['type.Class'].__wrap(super(Method, self).getParameterTypes())

    @overload
    def getDeclaringClass(self) -> 'type.Class':
        """public java.lang.Class com.badlogic.gdx.utils.reflect.Method.getDeclaringClass()"""
        return 'type.Class'.__wrap(super(Method, self).getDeclaringClass())

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @overload
    def isProtected(self) -> bool:
        """public boolean com.badlogic.gdx.utils.reflect.Method.isProtected()"""
        return bool.__wrap(super(Method, self).isProtected()) 
 
 
# CLASS: com.badlogic.gdx.utils.reflect.ReflectionException
from builtins import str
from pyquantum_helper import override
import java.lang.Object as __object
from builtins import type
import java.lang.Throwable as __Throwable
__Throwable = __Throwable
import java.io.PrintWriter as PrintWriter
import java.lang.StackTraceElement as StackTraceElement
import java.lang.StackTraceElement as __StackTraceElement
__StackTraceElement = __StackTraceElement
import com.badlogic.gdx.utils.reflect.ReflectionException as __ReflectionException
__ReflectionException = __ReflectionException
from typing import List
import java.lang.Long as __long
import java.lang.Class as __Class
__Class = __Class
import java.io.PrintStream as PrintStream
import java.lang.String as __String
__String = __String
import java.lang.String as __string
import java.lang.Object as __Object
__Object = __Object
import java.lang.Throwable as Throwable
import java.lang.Integer as __int
from builtins import bool
from builtins import int
 
class ReflectionException(__Exception, Exception):
    """com.badlogic.gdx.utils.reflect.ReflectionException"""
 
    @staticmethod
    def __wrap(java_value: __ReflectionException) -> 'ReflectionException':
        return ReflectionException(__dynamic__=java_value)
 
    #
    # DO NOT USE THIS. THIS IS FOR THE JAVA WRAPPER ONLY!
    #
    @overload
    def __init__(self, __dynamic__: __ReflectionException):
        """
        Dynamic initializer for ReflectionException.
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
    def getStackTrace(self) -> List['StackTraceElement']:
        """public java.lang.StackTraceElement[] java.lang.Throwable.getStackTrace()"""
        return List['StackTraceElement'].__wrap(super(Throwable, self).getStackTrace())

    @overload
    def __init__(self, arg0: 'Throwable'):
        """public com.badlogic.gdx.utils.reflect.ReflectionException(java.lang.Throwable)"""
        val = __ReflectionException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintWriter'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintWriter)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def notifyAll(self):
        """public final native void java.lang.Object.notifyAll()"""
        super(object, self).notifyAll()

    @override
    @overload
    def getMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getMessage()"""
        return str.__wrap(super(Throwable, self).getMessage())

    @override
    @overload
    def printStackTrace(self):
        """public void java.lang.Throwable.printStackTrace()"""
        super(Throwable, self).printStackTrace()

    @override
    @overload
    def getCause(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.getCause()"""
        return 'Throwable'.__wrap(super(Throwable, self).getCause())

    @overload
    def __init__(self, ):
        """public com.badlogic.gdx.utils.reflect.ReflectionException()"""
        val = __ReflectionException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def notify(self):
        """public final native void java.lang.Object.notify()"""
        super(object, self).notify()

    @override
    @overload
    def hashCode(self) -> int:
        """public native int java.lang.Object.hashCode()"""
        return int.__wrap(super(object, self).hashCode())

    @overload
    def equals(self, arg0: object) -> bool:
        """public boolean java.lang.Object.equals(java.lang.Object)"""
        return bool.__wrap(super(__object, self).equals(arg0))

    @override
    @overload
    def printStackTrace(self, arg0: 'PrintStream'):
        """public void java.lang.Throwable.printStackTrace(java.io.PrintStream)"""
        super(__Throwable, self).printStackTrace(arg0)

    @override
    @overload
    def toString(self) -> str:
        """public java.lang.String java.lang.Throwable.toString()"""
        return str.__wrap(super(Throwable, self).toString())

    @overload
    def __init__(self):
        """public com.badlogic.gdx.utils.reflect.ReflectionException()"""
        val = __ReflectionException()
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def __init__(self, arg0: str, arg1: 'Throwable'):
        """public com.badlogic.gdx.utils.reflect.ReflectionException(java.lang.String,java.lang.Throwable)"""
        val = __ReflectionException(arg0, arg1)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @override
    @overload
    def wait(self, arg0: int):
        """public final void java.lang.Object.wait(long) throws java.lang.InterruptedException"""
        super(__object, self).wait(__long.valueOf(arg0))

    @overload
    def __init__(self, arg0: str):
        """public com.badlogic.gdx.utils.reflect.ReflectionException(java.lang.String)"""
        val = __ReflectionException(arg0)
        self.__dict__ = val.__dict__
        self.__wrapper = val

    @overload
    def initCause(self, arg0: 'Throwable') -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.initCause(java.lang.Throwable)"""
        return 'Throwable'.__wrap(super(__Throwable, self).initCause(arg0))

    @override
    @overload
    def getClass(self) -> 'type.Class':
        """public final native java.lang.Class<?> java.lang.Object.getClass()"""
        return 'type.Class'.__wrap(super(object, self).getClass())

    @override
    @overload
    def addSuppressed(self, arg0: 'Throwable'):
        """public final synchronized void java.lang.Throwable.addSuppressed(java.lang.Throwable)"""
        super(__Throwable, self).addSuppressed(arg0)

    @override
    @overload
    def setStackTrace(self, arg0: 'StackTraceElement'):
        """public void java.lang.Throwable.setStackTrace(java.lang.StackTraceElement[])"""
        super(__Throwable, self).setStackTrace(arg0)

    @override
    @overload
    def wait(self):
        """public final void java.lang.Object.wait() throws java.lang.InterruptedException"""
        super(object, self).wait()

    @override
    @overload
    def getLocalizedMessage(self) -> str:
        """public java.lang.String java.lang.Throwable.getLocalizedMessage()"""
        return str.__wrap(super(Throwable, self).getLocalizedMessage())

    @override
    @overload
    def getSuppressed(self) -> List['Throwable']:
        """public final synchronized java.lang.Throwable[] java.lang.Throwable.getSuppressed()"""
        return List['Throwable'].__wrap(super(Throwable, self).getSuppressed())

    @override
    @overload
    def fillInStackTrace(self) -> 'Throwable':
        """public synchronized java.lang.Throwable java.lang.Throwable.fillInStackTrace()"""
        return 'Throwable'.__wrap(super(Throwable, self).fillInStackTrace())